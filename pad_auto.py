import padboard
#import uiautomator
import time
import subprocess
import os

start_time = time.time()

screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
subprocess.check_call(screencap_cmd, shell=True)

pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
subprocess.check_call(pull_cmd, shell=True)

# Nexus7(2012)
xa = 15
ya = 560
xb = 145
yb = 690
xs = 130
ys = 130


board = padboard.check_board(xa, ya, xb, yb, xs, ys, ".\screen.png", 6, 5)

p = subprocess.Popen(["c:/Users/hassy/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], stdout=subprocess.PIPE)
# p = subprocess.Popen(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun_old.exe", board], stdout=subprocess.PIPE)
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

def conv_x(i):
    return 15 + 65 + 130 * (int(i))

def conv_y(i):
    return 560 + 65 + 130 * (int(i))

def calc_i(flag, ary):
    pos_i = "\""
    #pos_i = "\\\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i]))
        else:
            pos_i += str(conv_y(ary[i]))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    #pos_i += "\\\""
    return pos_i

pos_x = calc_i("x", x)
pos_y = calc_i("y", y)

#pos_x = "470,600,600,470,470,470,470,600,600,470,470,340,340,340,340,340,210,80,80,80,80,210"
#pos_y = "1015,1015,1145,1145,1015,885,755,755,625,625,755,755,885,755,885,1015,1015,1015,885,755,625,625"

uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]

subprocess.check_call(uiautomator_cmd, shell=True)

elapsed_time = time.time() - start_time

print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
