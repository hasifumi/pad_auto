# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

WIN_USER_NAME = "fumio"
#WIN_USER_NAME = "hassy"

WIDTH = 6
HEIGHT = 5

MAX_TURN = 30
PLAYNUM = 400
SWIPE = 7

# RED = 1.0# {{{
# BLUE = 4.0
# GREEN = 1.0
# LIGHT = 1.0
# DARK = 2.0
# CURE = 3.0# }}}

PARMS = {# {{{
        'red'  : 0.0,
        'blue' : 0.0,
        'green': 0.0,
        'light': 1.0,
        'dark' : 0.0,
        'cure' : 1.0,
        '3colors'  : 0.0,
        '4colors'  : 2.0,
        '5colors'  : 0.0,
        '3colors+cure'  : 1.0,
        '4colors+cure'  : 0.0,
        '5colors+cure'  : 0.0,
        '4drops-red'  : 0.0,
        '4drops-blue' : 0.0,
        '4drops-green': 0.0,
        '4drops-light': 0.0,
        '4drops-dark' : 0.0,
        '4drops-cure' : 0.0,
        '5drops-red'  : 0.0,
        '5drops-blue' : 0.0,
        '5drops-green': 0.0,
        '5drops-light': 0.0,
        '5drops-dark' : 0.0,
        '5drops-cure' : 0.0,
        '1line-red'  : 0.0,
        '1line-blue' : 0.0,
        '1line-green': 0.0,
        '1line-light': 0.0,
        '1line-dark' : 0.0,
        '1line-cure' : 0.0,
        }# }}}

import padboard
#import uiautomator
import time
import subprocess
import os
import pad_search
import pazdracombo
from PIL import Image

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}

start_time = time.time()

screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
subprocess.check_call(screencap_cmd, shell=True)

pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
subprocess.check_call(pull_cmd, shell=True)

#path = "C:/Users/hassy/MyProject/python/pad_auto/screen.png" # Win10
#path = "C:/Users/fumio/MyProject/python/pad_auto/screen.png"  # Win7
path = "C:/Users/" + WIN_USER_NAME + "/MyProject/python/pad_auto/screen.png"

lap1_time = time.time()

pic = Image.open(path, 'r')
if pic.width == 800:# {{{
    is_nexus = True
else:
    is_nexus = False# }}}

#board = padboard.check_board(".\screen.png", 6, 5)
temp_board = padboard.check_board(".\screen.png", WIDTH, HEIGHT, 0)

board = pazdracombo.convert_h_w(temp_board)

# 確認用
print "[board]"
print print_board(WIDTH, HEIGHT, board)
print ""

x = []
y = []

def idx2xy(width, idx):# {{{
    return[int(idx/width), int(idx%width)]# }}}

#n_best = pad_search.Nbeam(6, 5, board, MAX_TURN, PLAYNUM, RED, BLUE, GREEN, LIGHT, DARK, CURE)
n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)

## 確認用
print "[combo]"
print print_board(WIDTH, HEIGHT, n_best.board)
print ""

for r in n_best.route:# {{{
    ans = idx2xy(WIDTH, r)
    x.append(ans[1])
    y.append(ans[0])# }}}

def conv_x(i):# {{{
    if is_nexus:
        return 15 + 65 + 130 * (int(i))
    else:
        return 5 + 90 + 180 * (int(i))# }}}

def conv_y(i):# {{{
    if is_nexus:
        return 560 + 65 + 130 * (int(i))
    else:
        return 850 + 90 + 180 * (int(i))# }}}

def calc_i(flag, ary):# {{{
    pos_i = "\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i]))
        else:
            pos_i += str(conv_y(ary[i]))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    return pos_i# }}}

pos_x = calc_i("x", x)
pos_y = calc_i("y", y)

print pos_x
print pos_y

#pos_x = "470,600,600,470,470,470,470,600,600,470,470,340,340,340,340,340,210,80,80,80,80,210"
#pos_y = "1015,1015,1145,1145,1015,885,755,755,625,625,755,755,885,755,885,1015,1015,1015,885,755,625,625"

swipe_time = str(SWIPE)

uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]


subprocess.check_call(uiautomator_cmd, shell=True)

elapsed_lap1_time = lap1_time - start_time
elapsed_time = time.time() - start_time

print("lap1_time:{0}".format(elapsed_lap1_time)) + "[sec]"
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
