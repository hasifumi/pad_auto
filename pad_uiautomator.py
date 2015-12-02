# -*- coding: utf-8 -*-

import uiautomator
import time

server = uiautomator.AutomatorServer()
device = uiautomator.Device()
#adb = uiautomator.Adb()

device.screen.on()

#print server.sdk_version()

def adb_cmd(device, cmd, *parm):
    c=[cmd]
    c.extend(parm)
    print (" ".join(c))
    return [s.decode("utf-8") for s in device.server.adb.cmd(*c).communicate()]

#adb_cmd(device, "shell", "screencap /sdcard/screen.png")
adb_cmd(device, "pull", "sdcard/screen.png")



#ss = server.adb
#if ss is None:
#    print "ss is None"

#print uiautomator.device.info
#
#print "screen on..."
#print uiautomator.device.screen.on()
#
#print "swiping..."
#x = uiautomator.device.displayWidth/2
#y0 = uiautomator.device.displayHeight/2
#y1 = y0/2
#y0 += y1/2
#x1 = x/2
#print x1
#print uiautomator.device.swipe(x1, y0, x, y0, steps=12)
#print uiautomator.device.swipe(x, y0, x, y1, steps=12)
#time.sleep(2)
