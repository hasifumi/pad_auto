#import padboard
#import uiautomator
#import time
import subprocess
# import os
# import pad_search
# import pazdracombo
# from PIL import Image

device_path = "/sdcard/screen.png"

def get_screenshot(device_path):
    screencap_cmd = ["adb", "shell", "screencap", device_path]
    subprocess.check_call(screencap_cmd, shell=True)

    pull_cmd = ["adb", "pull", device_path]
    subprocess.check_call(pull_cmd, shell=True)

if __name__ == '__main__':
    get_screenshot(device_path)
