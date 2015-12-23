# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#WIN_USER_NAME = "fumio"
#WIN_USER_NAME = "hassy"

# WIDTH = 5
# HEIGHT = 4
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
        '1line-red'  : 3.0,
        '1line-blue' : 0.0,
        '1line-green': 0.0,
        '1line-light': 10.0,
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

def conv_x(i, is_nexus, width=6):# {{{
    if is_nexus:
        if width == 5:
            return 15 + 78 + 155 * (int(i))
        elif width == 6:
            return 15 + 65 + 130 * (int(i))
    else:
        if width == 5:
            return 5  + 105 + 210 * (int(i))
        elif width == 6:
            return 5  +  90 + 180 * (int(i))
        elif width == 7:
            return 25 +  73 + 145 * (int(i))

def conv_y(i, is_nexus, width=6):# {{{
    if is_nexus:
        if width == 5:
            return 575 + 78 + 155 * (int(i))
        elif width == 6:
            return 560 + 65 + 130 * (int(i))
    else:
        if width == 5:
            return 865 + 105 + 210 * (int(i))
        elif width == 6:
            return 860 +  90 + 180 * (int(i))
        elif width == 7:
            return 850 +  73 + 145 * (int(i))

def calc_i(flag, ary, is_nexus, width):# {{{
    pos_i = "\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i], is_nexus, width))
        else:
            pos_i += str(conv_y(ary[i], is_nexus, width))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    return pos_i# }}}

def get_route(route, is_nexus, width):# {{{
    #print "get_route width:" + str(width)
    x = []
    y = []
    for r in route:
        ans = idx2xy(WIDTH, r)
        x.append(ans[1])
        y.append(ans[0])
    pos_x = calc_i("x", x, is_nexus, width)
    pos_y = calc_i("y", y, is_nexus, width)
    return (pos_x, pos_y)# }}}

def move_drop(pos_x, pos_y, swipe_time):# {{{
    uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]
    subprocess.check_call(uiautomator_cmd, shell=True)# }}}

#path = "C:/Users/" + WIN_USER_NAME + "/MyProject/python/pad_auto/screen.png"
path = ".\screen.png"

# main routine

end_flg = True

start_time = time.time()

while(end_flg):

    print "press any number key (1: get_ss & search, 2: move, else: exit)"
    input_test_word = input(">>>  ")
    if input_test_word == 1:
        print "getting screenshot ..."
        get_screenshot(device_path)
        #board = pazdracombo.convert_h_w(padboard.check_board(path, WIDTH, HEIGHT, 0))
        if WIDTH == 5:
            board = pazdracombo.convert_h_w_5x4(padboard.check_board(path, WIDTH, HEIGHT, 0))
            #print "WIDTH = 5: " + board
        elif WIDTH == 6:
            board = pazdracombo.convert_h_w_6x5(padboard.check_board(path, WIDTH, HEIGHT, 0))
            #print "WIDTH = 6: " + board
        elif WIDTH == 7:
            board = pazdracombo.convert_h_w_7x6(padboard.check_board(path, WIDTH, HEIGHT, 0))
            #print "WIDTH = 7: " + board
        print "searching ..."
        n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
        pos_x, pos_y = get_route(n_best.route, is_nexus(path), WIDTH)
        #print pos_x
        #print pos_y
        # 確認用
        print "[board]"
        print print_board(WIDTH, HEIGHT, board)
        print ""
        print "[combo]"
        print print_board(WIDTH, HEIGHT, n_best.board)
        print ""
    elif input_test_word == 2:
        print "moving drops ..."
        move_drop(pos_x, pos_y, str(SWIPE))
    else:
        print "pad_auto exit!!"
        end_flg = False

elapsed_time = time.time() - start_time
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
