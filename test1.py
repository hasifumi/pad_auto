import subprocess

#subprocess.check_call(['ls', '-l'], shell=True)
#subprocess.check_call(['pwd'], shell=True)
#subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/sample2.exe", '111', '2222'], shell=True)

#subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], shell=True)
#subprocess.check_call(["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", "\"90,350,90\"", "-e","\"y\"","\"625,625,755\""], shell=True)
#uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", "\"90,350,90\"", "-e","\"y\"","\"625,625,755\""]

x = ['1', '0', '1', '2', '2', '2']
y = ['0', '0', '0', '0', '1', '2']

def conv_x(i):
    return 15 + 65 + 130 * (int(i))

def conv_y(i):
    return 560 + 65 + 130 * (int(i))

def calc_i(flag, ary):
    pos_i = "\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i]))
        else:
            pos_i += str(conv_y(ary[i]))
        #pos_i += str(conv_i(ary[i]))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    return pos_i

#pos_x = calc_i("x", x)
#pos_y = calc_i("y", y)
#pos_y = pos_i(y)

#pos_x = "\"\\\"" + str(conv_i(x[0])) + "," + str(conv_i(x[1])) + "," + str(conv_i(x[2])) + "\"\\\""kk

pos_x = "470,600,600,470,470,470,470,600,600,470,470,340,340,340,340,340,210,80,80,80,80,210"
pos_y = "1015,1015,1145,1145,1015,885,755,755,625,625,755,755,885,755,885,1015,1015,1015,885,755,625,625"
print pos_x
print pos_y
#pos_x = "\"90,350,90,350\""
#pos_y = "\"625,625,755,900\""
uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]

subprocess.check_call(uiautomator_cmd, shell=True)

#board = "111112222233333444445555566666"
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
