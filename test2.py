import subprocess

screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
subprocess.check_call(screencap_cmd, shell=True)

pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
subprocess.check_call(pull_cmd, shell=True)


#import numpy
#from PIL import Image
#
#path = "C:/Users/hassy/MyProject/python/pad_auto/screen_nexus7.png"
#pic = Image.open(path, 'r')
#print "Nexus7 width: " + str(pic.width)
