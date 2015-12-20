# -*- coding: utf-8 -*-

import uiautomator
import time

server = uiautomator.AutomatorServer()
device = uiautomator.Device()
#adb = uiautomator.Adb()

device.screen.on()

print server.sdk_version()
#print server.screenshot_uri
server.screenshot("/sdcard/screen1.png")

def adb_cmd(device, cmd, *parm):
    c=[cmd]
    c.extend(parm)
    print (" ".join(c))
    return [s.decode("utf-8") for s in device.server.adb.cmd(*c).communicate()]

#adb_cmd(device, "shell", "screencap /sdcard/screen.png")
#adb_cmd(device, "pull", "/data/local/tmp/screen1.png")
#adb_cmd(device, "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e", "\"x\"", "\"90,350,90\"", "-e", "\"y\"", "\"625,625,755\"")
