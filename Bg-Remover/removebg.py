from rembg import remove
from PIL import Image
import os
output_dir = "BG REMOVES"
os.makedirs(output_dir, exist_ok=True)

files = os.listdir()
for file in files:
    try:
        if file.lower().endswith(('.png','.jpg','.jpeg')):
            img = Image.open(file)
            removed_bg = remove(img)
        if removed_bg.mode =="RGBA":
            removed_bg = removed_bg.convert("RGBA")
        filename, ext= os.path.splitext(file)
        removed_bg.save(os.path.join(output_dir,f"{filename}_removed{ext}"))
        print("DONE SCENE BRO")
    except Exception as e:
        pass