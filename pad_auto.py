import padboard
import uiautomator
import time
import subprocess

start_time = time.time()

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

board = padboard.check_board(xa, ya, xb, yb, xs, ys, ".\screen.png", 6, 5)


#subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], shell=True)

p = subprocess.Popen(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], stdout=subprocess.PIPE)
sout = []
while 1:
    c = p.stdout.readline()
    if not c:
        break
    #print c
    sout.append(c.rstrip())
p.wait()
print sout
x = []
y = []
for i,v in enumerate(sout):
    x.append(v[2])
    y.append(v[6])
print x
print y

elapsed_time = time.time() - start_time
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

#path = "C:/Users/fumio/MyProject/python/pad_auto/image/pazdra_board.png"
