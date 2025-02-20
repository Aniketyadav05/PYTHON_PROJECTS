import pyautogui
import cv2
import numpy as np
from PIL import Image, ImageGrab

# Take a screenshot of the full screen
screenshot = ImageGrab.grab()
img = np.array(screenshot)

# Define the desired width
desired_width = 1500
aspect_ratio = img.shape[1] / img.shape[0]
desired_height = int(desired_width / aspect_ratio)

# Resize image while maintaining aspect ratio
img = cv2.resize(img, (desired_width, desired_height))

# Get new height and width
height, width = img.shape[:2]

# Define region to capture
region_width = int(width * 0.25)  # Ensure it's an integer
center_x = width // 2

start_x = max(0, int(center_x - (region_width / 2)))  # Ensure within bounds
end_x = min(width, int(center_x + (region_width / 2)))

start_y = height
end_y = max(0, int(height - (height * 0.30)))  # Prevent negative values

# Ensure selected_region is valid
if start_x < end_x and end_y < start_y:
    selected_region = img[end_y:start_y, start_x:end_x]

    # Convert and save the image
    screenshot = Image.fromarray(selected_region)
    screenshot.save("screenshot.png")
    print("Screenshot saved as screenshot.png")
else:
    print("Invalid region coordinates. Adjust the calculations.")
