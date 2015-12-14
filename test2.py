import subprocess

#screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
#subprocess.check_call(screencap_cmd, shell=True)
#
#pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
#subprocess.check_call(pull_cmd, shell=True)


#import numpy
#from PIL import Image
#
#path = "C:/Users/hassy/MyProject/python/pad_auto/screen_nexus7.png"
#pic = Image.open(path, 'r')
#print "Nexus7 width: " + str(pic.width)

pos_x = "90,350,90"
pos_y = "625,625,760"
swipe_time = "5"

#uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]
uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]


subprocess.check_call(uiautomator_cmd, shell=True)

