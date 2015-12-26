# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#WIN_USER_NAME = "fumio"
#WIN_USER_NAME = "hassy"

WIDTH = 6
HEIGHT = 5

MAX_TURN = 40
PLAYNUM = 500
SWIPE = 4

DEFAULT_PARMS = {# {{{
        'name'  : "default",
        'red'  : 0.0,
        'blue' : 0.0,
        'green': 0.0,
        'light': 0.0,
        'dark' : 0.0,
        'cure' : 0.0,
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
        '1line-red'  : 0.0,
        '1line-blue' : 0.0,
        '1line-green': 0.0,
        '1line-light': 0.0,
        '1line-dark' : 0.0,
        '1line-cure' : 0.0,
        }# }}}

PARMS_PATTERN = {
        'saria, tall': {
            'red': 5.0,
            'light': 10.0,
            'cure': 5.0,
            '4drops-red' : 5.0,
            '4drops-light' : 10.0,
            '1line-red': 10.0,
            '1line-light': 50.0,
            },
        'blue-sonia, ryune': {
            'blue': 10.0,
            'dark': 5.0,
            'cure': 5.0,
            '5drops-blue': 50.0,
            '1line-blue': 50.0,
            '1line-dark': 10.0,
            },
        }

PARMS = DEFAULT_PARMS

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
            return 25 +  73 + 145 * (int(i))# }}}

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
            return 850 +  73 + 145 * (int(i))# }}}

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

def getting_screenshot(device_path, path, WIDTH, HEIGHT):# {{{
    print "getting screenshot ..."
    start_time = time.time()
    get_screenshot(device_path)
    if WIDTH == 5:
        board = pazdracombo.convert_h_w_5x4(padboard.check_board(path, WIDTH, HEIGHT, 0))
    elif WIDTH == 6:
        board = pazdracombo.convert_h_w_6x5(padboard.check_board(path, WIDTH, HEIGHT, 0))
    elif WIDTH == 7:
        board = pazdracombo.convert_h_w_7x6(padboard.check_board(path, WIDTH, HEIGHT, 0))
    elapsed_time = time.time() - start_time
    print("getting time:{0}".format(elapsed_time)) + "[sec]"
    return board# }}}

def searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS):# {{{
    print "searching ..."
    start_time = time.time()
    n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    pos_x, pos_y = get_route(n_best.route, is_nexus(path), WIDTH)
    # 確認用
    print "[board]"
    print print_board(WIDTH, HEIGHT, board)
    print ""
    print "[combo]"
    print print_board(WIDTH, HEIGHT, n_best.board)
    print ""
    elapsed_time = time.time() - start_time
    print("searching time:{0}".format(elapsed_time)) + "[sec]"
    return (pos_x, pos_y)# }}}

def moving(pos_x, pos_y, SWIPE):# {{{
    print "moving drops ..."
    start_time = time.time()
    move_drop(pos_x, pos_y, str(SWIPE))
    elapsed_time = time.time() - start_time
    print("moving time:{0}".format(elapsed_time)) + "[sec]"# }}}

def select_board(WIDTH, HEIGHT):# {{{
    print " WIDTH: " + str(WIDTH) + ", HEIGHT: " + str(HEIGHT)
    print "select WIDTH x HEIGHT (1: 5x4, 2: 6x5, 3: 7x6, ... 99: cancel, else:default(6x5) )"
    input_test_word = input(">>>  ")
    if input_test_word == 1:
        return (5, 4)
    elif input_test_word == 2:
        return (6, 5)
    elif input_test_word == 3:
        print " sorry, no implement 7x6 board"
        return (WIDTH, HEIGHT)
        #return (7, 6)
    elif input_test_word == 99:
        print "canceled changing board"
        return (WIDTH, HEIGHT)
    else:
        return (6, 5)# }}}

def select_parms_pattern(PARMS):# {{{
    print "current pattern name = " + PARMS['name']
    cnt = 0
    patterns = {}
    patterns_str = ""
    for k in PARMS_PATTERN.keys():
        patterns[cnt] = k
        patterns_str = patterns_str + str(cnt + 1) + ": " + k + ", "
        cnt += 1
    patterns_str = patterns_str + ", 99: cancel"
    print "select parms pattern (" + patterns_str + ")"
    input_test_word = input(">>>  ")
    input_test_word -= 1
    if input_test_word == 99 - 1:
        print "canceled changing parms"
        pass
    elif PARMS_PATTERN.has_key(patterns[input_test_word]):
        PARMS['name'] = patterns[input_test_word]
        for k in PARMS_PATTERN[patterns[input_test_word]].keys():
            if PARMS.has_key(k):
                PARMS[k] = PARMS_PATTERN[patterns[input_test_word]][k]
    return PARMS# }}}

path = ".\screen.png"

# main routine

end_flg = True


while(end_flg):

    print "press key (1: get_ss, 2: search, 3: move,  4: get_ss & search, 5: search & move, "
    print "           6: get_ss & search & move, 7: select pattern, 8: change WIDTH & HEIGHT, 99: exit )"
    input_test_word = input(">>>  ")
    if input_test_word == 1:
        board = getting_screenshot(device_path, path, WIDTH, HEIGHT)
    elif input_test_word == 2:
        pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    elif input_test_word == 3:
        moving(pos_x, pos_y, SWIPE)
    if input_test_word == 4:
        board = getting_screenshot(device_path, path, WIDTH, HEIGHT)
        pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    elif input_test_word == 5:
        pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
        moving(pos_x, pos_y, SWIPE)
    elif input_test_word == 6:
        board = getting_screenshot(device_path, path, WIDTH, HEIGHT)
        pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
        moving(pos_x, pos_y, SWIPE)
    elif input_test_word == 7:
        PARMS = select_parms_pattern(PARMS)
    elif input_test_word == 8:
        WIDTH, HEIGHT = select_board(WIDTH, HEIGHT)
        print " WIDTH: " + str(WIDTH) + ", HEIGHT: " + str(HEIGHT)
    elif input_test_word == 99:
        print "pad_auto exit!!"
        end_flg = False
    else:
        print "press correct key!!"
        #end_flg = False

