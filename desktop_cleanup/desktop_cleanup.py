import shutil
import os

screenshot_dir = "C:/Users/XXX/Desktop/ScreenShots"
desktop_dir = "C:/Users/XXXX/Desktop"

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print("test")

for file in os.listdir(desktop_dir):
    if file.startswith("Screenshot"):
        shutil.move(file,screenshot_dir)
        