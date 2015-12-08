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

#adb_cmd(device, "shell", "screencap /sdcard/screen.png")
#adb_cmd(device, "pull", "sdcard/screen.png")
#
##time.sleep(5)
#
## Nexus7(2012)
#xa = 15
#ya = 560
#xb = 145
#yb = 690
#xs = 130
#ys = 130
#
#board = padboard.check_board(xa, ya, xb, yb, xs, ys, ".\screen.png", 6, 5)
#
#
##subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], shell=True)
#
#p = subprocess.Popen(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], stdout=subprocess.PIPE)
#sout = []
#while 1:
#    c = p.stdout.readline()
#    if not c:
#        break
#    #print c
#    sout.append(c.rstrip())
#p.wait()
#print sout
#x = []
#y = []
#for i,v in enumerate(sout):
#    x.append(v[2])
#    y.append(v[6])
#print x
#print y
#print len(x)
#
#def conv_x(i):
#    return 15 + 65 + 130 * (int(i))
#
#def conv_y(i):
#    return 560 + 65 + 130 * (int(i))
#
#def calc_i(flag, ary):
#    pos_i = "\""
#    #pos_i = "\\\""
#    for i,v in enumerate(ary):
#        if flag == "x":
#            pos_i += str(conv_x(ary[i]))
#        else:
#            pos_i += str(conv_y(ary[i]))
#        pos_i += ","
#    pos_i = pos_i.rstrip(",")
#    pos_i += "\""
#    #pos_i += "\\\""
#    return pos_i
#
#pos_x = calc_i("x", x)
#pos_y = calc_i("y", y)

pos_x = "470,600,600,470,470,470,470,600,600,470,470,340,340,340,340,340,210,80,80,80,80,210"
pos_y = "1015,1015,1145,1145,1015,885,755,755,625,625,755,755,885,755,885,1015,1015,1015,885,755,625,625"

print pos_x
print pos_y
#uiautomator_cmd = "uiautomator runtest UiAutomator.jar -c com.hahahassy.android.UiAutomator#swipe -e \"x\" " + pos_x + " -e \"y\" " + pos_y
#print uiautomator_cmd
#adb_cmd(device, "shell", uiautomator_cmd)
#uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]
##
#subprocess.check_call(uiautomator_cmd, shell=True)


uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]

subprocess.check_call(uiautomator_cmd, shell=True)

elapsed_time = time.time() - start_time
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

#path = "C:/Users/fumio/MyProject/python/pad_auto/image/pazdra_board.png"
