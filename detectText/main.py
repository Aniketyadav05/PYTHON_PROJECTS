import cv2
import pytesseract
import re
import datetime
import pyautogui
import os
import sys
import shutil
import time
from dotenv import load_dotenv
from notifypy import Notify
import platform

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

debugMode = os.getenv('DEBUG') == '1'

args = sys.argv
mode = 'capture'

last_player_name = None  # Track last detected player

if len(args) >= 2:
    mode = args[1]

def _run():
    global last_player_name

    if mode == 'test':
        file = 'test.jpeg'
    else:
        file = take_screenshot()

    img = cv2.imread(file)

    # Resize image
    desired_width = 1500
    aspect_ratio = img.shape[1] / img.shape[0]
    desired_height = int(desired_width / aspect_ratio)
    img = cv2.resize(img, (desired_width, desired_height))

    # Define region to extract player name
    height, width = img.shape[:2]
    region_width = (width * 0.25)  
    center_x = width // 2  

    start_x = int(center_x - (region_width / 2))
    end_x = int(center_x + (region_width / 2))
    start_y = height
    end_y = height - (height * 0.30)

    selected_region = img[int(end_y):int(start_y), int(start_x):int(end_x)]

    # Extract player name
    player_name = extract_player_name(selected_region)
    fallback_image = os.path.join('players', 'default.jpeg')

    if not os.path.exists(fallback_image):
        display_notification("Error: Default image missing!", "")
    else:
        if player_name == '':
            display_notification('No player found!', '')
            shutil.copy(fallback_image, os.getenv('TARGET_FOLDER', '') + 'activePlayer.jpeg')
        else:
            player_image = find_file('players', player_name)
            print(f"Detected Player: {player_name}")

            if last_player_name == player_name:
                display_notification("Existing player: ", player_name)
                shutil.copy(player_image, os.getenv('TARGET_FOLDER', '') + 'activePlayer.jpeg')

            elif player_image is not None:
                display_notification("Player found: ", player_name)
                shutil.copy(player_image, os.getenv('TARGET_FOLDER', '') + 'activePlayer.jpeg')
                last_player_name = player_name
            else:
                display_notification("No image for this player found, using default image", '')
                shutil.copy(fallback_image, os.getenv('TARGET_FOLDER', '') + 'activePlayer.jpeg')

    if debugMode == False and mode != 'test':
        os.unlink(file)

def find_file(folder_path, file_name):
    """ Search for an image that matches the extracted player name """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[0].lower() == file_name.lower():  # Case-insensitive match
                return os.path.join(root, file)
    return None

def take_screenshot():
    temp_dir = '.temp_screens'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    file_name = f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')}.png"
    file_path = os.path.join(temp_dir, file_name)

    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)

    return file_path

def extract_player_name(region):
    """ Extracts the player's name using OCR and filters out unwanted text """
    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = region.copy()

    matched_name = ''

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area < 100:
            continue
        
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped, config="--psm 6")
        lines = text.split('\n')

        for line in lines:
            line = line.strip()

            # Ignore UID patterns
            uid_pattern = r'\b(UID|U1D|u1|UI|ID|ui0|uio|ui|u10|ulb)\b'
            if re.search(uid_pattern, line, flags=re.IGNORECASE):
                continue  # Skip UID-like strings

            # Ignore empty or numeric strings (most likely not a name)
            if not line or line.isdigit():
                continue
            
            matched_name = line  # Assume first valid text is the player name
            break

        if matched_name:
            break  # Stop after finding the first valid name

    return matched_name

def display_notification(title, message):
    print(f"{title}: {message}")
    if platform.system() != 'Windows':
        notification = Notify()
        notification.title = title
        notification.message = message
        notification.send()

if mode == 'live':
    while True:
        _run()
else:
    _run()
