#import subprocess
#
#screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
#subprocess.check_call(screencap_cmd, shell=True)
#
#pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
#subprocess.check_call(pull_cmd, shell=True)

# ============================================================

import uiautomator

device = uiautomator.Device()

device.screen.on()
device.screenshot("screencap.png")
