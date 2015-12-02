import padboard
import uiautomator
import time

server = uiautomator.AutomatorServer()
device = uiautomator.Device()

device.screen.on()

def adb_cmd(device, cmd, *parm):
    c=[cmd]
    c.extend(parm)
    #print (" ".join(c))
    return [s.decode("utf-8") for s in device.server.adb.cmd(*c).communicate()]

adb_cmd(device, "shell", "screencap /sdcard/screen.png")
adb_cmd(device, "pull", "sdcard/screen.png")

#time.sleep(5)

# Nexus7(2012)
xa = 15
ya = 560
xb = 145
yb = 690
xs = 130
ys = 130

padboard.check_board(xa, ya, xb, yb, xs, ys, ".\screen.png", 6, 5)



#path = "C:/Users/fumio/MyProject/python/pad_auto/image/pazdra_board.png"
