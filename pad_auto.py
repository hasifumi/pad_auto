# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

WIN_USER_NAME = "fumio"
#WIN_USER_NAME = "hassy"

WIDTH = 6
HEIGHT = 5

MAX_TURN = 35
PLAYNUM = 400
SWIPE = 5

# RED = 1.0# {{{
# BLUE = 4.0
# GREEN = 1.0
# LIGHT = 1.0
# DARK = 2.0
# CURE = 3.0# }}}

PARMS = {# {{{
        'red'  : 1.0,
        'blue' : 0.0,
        'green': 0.0,
        'light': 5.0,
        'dark' : 0.0,
        'cure' : 1.0,
        '3colors'  : 0.0,
        '4colors'  : 0.0,
        '5colors'  : 0.0,
        '3colors+cure'  : 0.0,
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
        '1line-red'  : 5.0,
        '1line-blue' : 0.0,
        '1line-green': 0.0,
        '1line-light': 5.0,
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

device_path = "/sdcard/screen.png"
def get_screenshot(device_path):# {{{
    screencap_cmd = ["adb", "shell", "screencap", device_path]
    subprocess.check_call(screencap_cmd, shell=True)

    pull_cmd = ["adb", "pull", device_path]
    subprocess.check_call(pull_cmd, shell=True)

    return# }}}

def is_nexus(path):# {{{
    pic = Image.open(path, 'r')
    if pic.width == 800:
        return True
    else:
        return False# }}}

def idx2xy(width, idx):# {{{
    return[int(idx/width), int(idx%width)]# }}}

def conv_x(i, is_nexus):# {{{
    if is_nexus:
        return 15 + 65 + 130 * (int(i))
    else:
        return 5 + 90 + 180 * (int(i))# }}}

def conv_y(i, is_nexus):# {{{
    if is_nexus:
        return 560 + 65 + 130 * (int(i))
    else:
        return 850 + 90 + 180 * (int(i))# }}}

def calc_i(flag, ary, is_nexus):# {{{
    pos_i = "\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i], is_nexus))
        else:
            pos_i += str(conv_y(ary[i], is_nexus))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    return pos_i# }}}

def get_route(route, is_nexus):# {{{
    x = []
    y = []
    for r in route:
        ans = idx2xy(WIDTH, r)
        x.append(ans[1])
        y.append(ans[0])
    pos_x = calc_i("x", x, is_nexus)
    pos_y = calc_i("y", y, is_nexus)
    return (pos_x, pos_y)# }}}

def move_drop(pos_x, pos_y, swipe_time):# {{{
    uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]
    subprocess.check_call(uiautomator_cmd, shell=True)# }}}

path = "C:/Users/" + WIN_USER_NAME + "/MyProject/python/pad_auto/screen.png"
# main routine

start_time = time.time()

get_screenshot(device_path)

board = pazdracombo.convert_h_w(padboard.check_board(".\screen.png", WIDTH, HEIGHT, 0))

n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
pos_x, pos_y = get_route(n_best.route, is_nexus(path))

# 確認用
print "[board]"
print print_board(WIDTH, HEIGHT, board)
print ""

print "[combo]"
print print_board(WIDTH, HEIGHT, n_best.board)
print ""

#print "press any key"
#input_test_word = raw_input(">>>  ")
#print "key: " + str(input_test_word)

move_drop(pos_x, pos_y, str(SWIPE))

elapsed_lap1_time = lap1_time - start_time
elapsed_time = time.time() - start_time
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
