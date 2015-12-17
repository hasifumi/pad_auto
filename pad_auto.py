# -*- coding: utf-8 -*-

MAX_TURN = 30
PLAYNUM = 400
SWIPE = 5

import padboard
#import uiautomator
import time
import subprocess
import os
import pad_search
import pazdracombo
from PIL import Image

def print_board(width, height, board):
    for h in range(height):
        print board[h*width:h*width+width]
    return 1

start_time = time.time()

screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
subprocess.check_call(screencap_cmd, shell=True)

pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
subprocess.check_call(pull_cmd, shell=True)

#path = "C:/Users/hassy/MyProject/python/pad_auto/screen.png" # Win10
path = "C:/Users/fumio/MyProject/python/pad_auto/screen.png"  # Win7

lap1_time = time.time()

pic = Image.open(path, 'r')
if pic.width == 800:
    is_nexus = True
else:
    is_nexus = False

#board = padboard.check_board(".\screen.png", 6, 5)
temp_board = padboard.check_board(".\screen.png", 6, 5, 0)

board = pazdracombo.convert_h_w(temp_board)

# 確認用
print "[board]"
print print_board(6, 5, board)
print ""

x = []
y = []

## p = subprocess.Popen(["c:/Users/hassy/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], stdout=subprocess.PIPE)     # Win10
#p = subprocess.Popen(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun_old.exe", board], stdout=subprocess.PIPE)   # Win7
#sout = []
#while 1:
#    c = p.stdout.readline()
#    if not c:
#        break
#    sout.append(c.rstrip())
#p.wait()
#print sout
#for i,v in enumerate(sout):
#    x.append(v[2])
#    y.append(v[6])

def idx2xy(width, idx):
    return[int(idx/width), int(idx%width)]

n_best = pad_search.Nbeam(6, 5, board, MAX_TURN, PLAYNUM)


## 確認用
print ""
print "[combo]"
print print_board(6, 5, n_best.board)
print ""

for r in n_best.route:
    ans = idx2xy(6, r)
    x.append(ans[1])
    y.append(ans[0])

print x
print y

def conv_x(i):
    #return 15 + 65 + 130 * (int(i))
    if is_nexus:
        return 15 + 65 + 130 * (int(i))
    else:
        return 5 + 90 + 180 * (int(i))

def conv_y(i):
    #return 560 + 65 + 130 * (int(i))
    if is_nexus:
        return 560 + 65 + 130 * (int(i))
    else:
        return 850 + 90 + 180 * (int(i))

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

print pos_x
print pos_y

#pos_x = "470,600,600,470,470,470,470,600,600,470,470,340,340,340,340,340,210,80,80,80,80,210"
#pos_y = "1015,1015,1145,1145,1015,885,755,755,625,625,755,755,885,755,885,1015,1015,1015,885,755,625,625"

#uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y]

swipe_time = str(SWIPE)

uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]


subprocess.check_call(uiautomator_cmd, shell=True)

elapsed_lap1_time = lap1_time - start_time
elapsed_time = time.time() - start_time

print("lap1_time:{0}".format(elapsed_lap1_time)) + "[sec]"
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
