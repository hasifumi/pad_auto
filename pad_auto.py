# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#WIN_USER_NAME = "fumio"# {{{
#WIN_USER_NAME = "hassy"# }}}

WIDTH = 6# {{{
HEIGHT = 5# }}}

# MAX_TURN = 45# {{{
# PLAYNUM = 500
# SWIPE = 4# }}}

DEFAULT_GAME_PARMS = {# {{{
        'MAX_TURN' : 50,
        'PLAYNUM' : 30,
        #'SWIPE' : 4,
        'SWIPE' : 0.001,
        }# }}}

GAME_PARMS_PATTERN = {# {{{
        'default' : {
            'MAX_TURN' : 35,
            'PLAYNUM'  : 25,
            'SWIPE'    : 4,
            },
        'win_tablet' : {
            'MAX_TURN' : 30,
            'PLAYNUM'  : 20,
            'SWIPE'    : 5,
            },
        'long_thinking' : {
            'MAX_TURN' : 50,
            'PLAYNUM'  : 50,
            'SWIPE'    : 5,
            },
        }# }}}

def show_game_parms():# {{{
    print "show game parms ... "
    print " MAX_TURN : " + str(MAX_TURN)
    print " PLAYNUM  : " + str(PLAYNUM)
    print " SWIPE    : " + str(SWIPE)# }}}

def set_game_parms(pattern):# {{{
    if GAME_PARMS_PATTERN.has_key(pattern):
        if GAME_PARMS_PATTERN[pattern].has_key('MAX_TURN') and GAME_PARMS_PATTERN[pattern].has_key('PLAYNUM') and GAME_PARMS_PATTERN[pattern].has_key('SWIPE'):
            print "set game parms ... "
            print " name     : " + str(pattern)
            print " MAX_TURN : " + str(GAME_PARMS_PATTERN[pattern]['MAX_TURN'])
            print " PLAYNUM  : " + str(GAME_PARMS_PATTERN[pattern]['PLAYNUM'])
            print " SWIPE    : " + str(GAME_PARMS_PATTERN[pattern]['SWIPE'])
            return (GAME_PARMS_PATTERN[pattern]['MAX_TURN'], GAME_PARMS_PATTERN[pattern]['PLAYNUM'], GAME_PARMS_PATTERN[pattern]['SWIPE'])
    else:
        return (40, 500, 4)# }}}

# MAX_TURN, PLAYNUM, SWIPE = set_game_parms('default')
#show_game_parms()

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

PARMS_PATTERN = {# {{{
        'default': {
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
            },
        'saria, tall': {
            'red': 2.0,
            'green': 3.0,
            'light': 3.0,
            'cure': 5.0,
            '4drops-red' : 5.0,
            '4drops-blue': 3.0,
            '4drops-green': 5.0,
            '4drops-light' : 10.0,
            '5drops-red' : -5.0,
            '5drops-green' : -10.0,
            '5drops-light' : -10.0,
            '1line-red': 10.0,
            '1line-light': 30.0,
            },
        'blue-sonia, ryune': {
            'blue': 10.0,
            'dark': 5.0,
            'cure': 5.0,
            '4drops-blue': 10.0,
            '4drops-light' : 5.0,
            '4drops-dark' : 5.0,
            '5drops-blue': 50.0,
            '1line-blue': 50.0,
            '1line-dark': 10.0,
            },
        'basteto/shiva': {
            'red': 10.0,
            'green': 10.0,
            'cure': 5.0,
            '4drops-red': 50.0,
            '4drops-blue': 50.0,
            '4drops-green': 50.0,
            '1line-red': -10.0,
            '1line-green': -10.0,
            },
        'athena': {
            'light': 10.0,
            'green': 5.0,
            'cure': 5.0,
            '4drops-green': 10.0,
            '4drops-light': 30.0,
            },
        'zeroge-4drops': {
            'dark': 30.0,
            'blue': 10.0,
            'cure': 10.0,
            '4drops-dark': 20.0,
            '1line-dark': -10.0,
            },
        'zeroge': {
            'dark': 30.0,
            'blue': 10.0,
            'cure': 10.0,
            '1line-dark': -10.0,
            },
        'isis': {
            '3colors': 10.0,
            },
        'izuizu, ryune': {
            'dark': 5.0,
            'blue': 15.0,
            'cure': 10.0,
            '4drops-blue': 20.0,
            '4drops-dark': 10.0,
            '1line-blue': -10.0,
            '1line-dark': -10.0,
            },
        'horus': {
            'cure': 5.0,
            '4colors'  : 10.0,
            '5colors'  : 5.0,
            '3colors+cure'  : 5.0,
            '4colors+cure'  : 5.0,
            '5colors+cure'  : 5.0,
            },
        }# }}}

ANDROID_TERM = "SC-03L"

import padboard
import uiautomator
import time
import subprocess
import os
import pad_search
import pazdracombo
from PIL import Image
from PIL import ImageGrab
import pyautogui
import win32gui
import win32api
import call_julia_prog

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}

# device_path = "/sdcard/screen.png"
def get_screenshot(device_path):# {{{
    screencap_cmd = ["adb", "shell", "screencap", device_path]
    subprocess.check_call(screencap_cmd, shell=True)

    pull_cmd = ["adb", "pull", device_path]
    subprocess.check_call(pull_cmd, shell=True)

    return# }}}

def set_activeWindow(window_id):# {{{

    VK_TAB = 0x09
    VK_SHIFT = 0x10
    VK_MENU = 0x12
    KEYEVENTF_KEYUP = 0x2
    start = time.time()

    while True:
        hw = win32gui.GetForegroundWindow()
        # print(hw)
        if window_id == hw:
            break
        time.sleep(0.5)
        if time.time() - start > 5:
            print("fail set_activeWindow()!")
            break

        win32api.keybd_event(VK_MENU, 0, 0)
        win32api.keybd_event(VK_SHIFT, 0, 0)
        win32api.keybd_event(VK_TAB, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(VK_TAB, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP)
        time.sleep(0.1)# }}}

def get_screenshot_new(path, android_term):# {{{
    a = win32gui.FindWindow(None, android_term)
    print(a)
    print(win32gui.GetWindowText(a))
    if a != 0:
        win32gui.SetActiveWindow(a)
        win32gui.BringWindowToTop(a)
        set_activeWindow(a)
        if android_term == "SHV32":
            win32gui.MoveWindow(a, 700, 50, 464, 839, True)
        else:
            win32gui.MoveWindow(a, 700, 50, 392, 839, True)
    time.sleep(2)
    # win32gui.MoveWindow(a, 700, 50, 392, 839, True)
    rect = win32gui.GetWindowRect(a)
    print(rect)
    ImageGrab.grab(rect).save(path)
    print("get screenshot")# }}}

def getting_screenshot(device_path, path, WIDTH, HEIGHT, use_old=0, android_term="SC-03L"):# {{{
    if use_old == 0:
        print "getting screenshot ..."
        start_time = time.time()
        get_screenshot_new(path, android_term)
    else:
        print "using old screenshot ..."
        start_time = time.time()

    elapsed_time = time.time() - start_time
    print("getting time:{0}".format(elapsed_time)) + "[sec]"

    print "checking board ..."
    start_time = time.time()
    if WIDTH == 5:
        board, key1, key2 = padboard.check_board(path, WIDTH, HEIGHT, 0)
        board = pazdracombo.convert_h_w_5x4(board)
    elif WIDTH == 6:
        board, key1, key2 = padboard.check_board(path, WIDTH, HEIGHT, 0)
        board = pazdracombo.convert_h_w_6x5(board)
    elif WIDTH == 7:
        board, key1, key2 = padboard.check_board(path, WIDTH, HEIGHT, 0)
        board = pazdracombo.convert_h_w_7x6(board)
        #print "7x6 board: " + str(board)
        #print " sorry, no implement 7x6 board"
        #return (WIDTH, HEIGHT)
    elapsed_time = time.time() - start_time
    print("checking time:{0}".format(elapsed_time)) + "[sec]"
    print("key1:"+key1)
    print("key2:"+key2)
    return board, key1, key2 # }}}

def is_nexus(path):# {{{
    pic = Image.open(path, 'r')
    #if pic.width == 800:
    if pic.size[0] == 800:
        return True
    else:
        return False# }}}

def idx2xy(width, idx):# {{{
    return[int(idx/width), int(idx%width)]# }}}

def idx2xy_new(width, idx):# {{{
    return[int(idx%width), int(idx/width)]# }}}

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
            #return 860 +  90 + 180 * (int(i))
            return 1370 +  90 + 180 * (int(i))
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

def calc_i_new(ary, key1_size_width, key2_cols_rows, sc03l_x=700, sc03l_y=50):# {{{
    route = []
    if padboard.pic_parm.has_key(key1_size_width):
        if padboard.pic_parm[key1_size_width].has_key(key2_cols_rows):
            xa = padboard.pic_parm[key1_size_width][key2_cols_rows]['xa']
            ya = padboard.pic_parm[key1_size_width][key2_cols_rows]['ya']
            xs = padboard.pic_parm[key1_size_width][key2_cols_rows]['xs']
            ys = padboard.pic_parm[key1_size_width][key2_cols_rows]['ys']
    print("xa:"+str(xa))
    print("ya:"+str(ya))
    print("xs:"+str(xs))
    print("ys:"+str(ys))
    for a in ary:
        ary_x = xa + (xs/2) + (xs * a[0]) + sc03l_x
        ary_y = ya + (ys/2) + (ys * a[1]) + sc03l_y
        route.append([ary_x, ary_y])
    print("route:")
    print(route)
    return route# }}}

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

def board_a2i(board):# {{{
    board_i = ""
    for i in board:
        if i == "r":
            board_i += "1"
        elif i == "b":
            board_i += "2"
        elif i == "g":
            board_i += "3"
        elif i == "l":
            board_i += "4"
        elif i == "d":
            board_i += "5"
        elif i == "c":
            board_i += "6"
    # print board_i
    return board_i# }}}

def searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, android_term):# {{{
    if board is None:
        board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1, android_term)  # すでに取得済みのscreenshotを利用する
    print "searching ..."
    start_time = time.time()

    # n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    # pos_x, pos_y = get_route(n_best.route, is_nexus(path), WIDTH)
    # n_best_route_xy = []
    # for r in n_best.route:
    #     n_best_route_xy.append(idx2xy_new(WIDTH, r))
    # # 確認用
    # print "[board]"
    # print print_board(WIDTH, HEIGHT, board)
    # print ""
    # print "[combo]"
    # print print_board(WIDTH, HEIGHT, n_best.board)
    # print ""
    # print "[route]"
    # print n_best.route
    # print n_best_route_xy
    # # print(pos_x)
    # # print(pos_y)
    # # print ""

    n_best_route_xy = call_julia_prog.call_julia_prog(board_a2i(board), WIDTH, HEIGHT)
    # n_best_route_xy = call_julia_prog.call_julia_prog(board_a2i(board), WIDTH, HEIGHT, "1") # flg_delete_row is on(1)

    elapsed_time = time.time() - start_time
    print("searching time:{0}".format(elapsed_time)) + "[sec]"
    #return (pos_x, pos_y)
    # print(n_best_route_xy)
    return (n_best_route_xy)# }}}

def moving(pos_x, pos_y, SWIPE):# {{{
    print "moving drops ..."
    start_time = time.time()
    print "pos_x: " + str(pos_x)
    print "pos_y: " + str(pos_y)
    move_drop(pos_x, pos_y, str(SWIPE))
    elapsed_time = time.time() - start_time
    print("moving time:{0}".format(elapsed_time)) + "[sec]"# }}}

def moving_new(route_xy, key1_size_width, key2_cols_rows, android_term):# {{{
    print "moving drops ..."
    start_time = time.time()
    route = calc_i_new(route_xy, key1_size_width, key2_cols_rows)
    move_drop_new(route, 0.1, android_term)
    elapsed_time = time.time() - start_time
    print("moving time:{0}".format(elapsed_time)) + "[sec]"# }}}

def move_drop(pos_x, pos_y, swipe_time):# {{{
    uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]
    subprocess.check_call(uiautomator_cmd, shell=True)# }}}

def move_drop_new(route, dur, android_term):# {{{
    a = win32gui.FindWindow(None, android_term)
    print(win32gui.GetWindowText(a))
    if a != 0:
        win32gui.SetActiveWindow(a)
        win32gui.BringWindowToTop(a)
        set_activeWindow(a)
    time.sleep(2)

    pyautogui.mouseDown(route[0][0], route[0][1], button='left')
    for r in route:
        pyautogui.moveTo(r[0], r[1], duration=dur)
    pyautogui.mouseUp(r[0], r[1], button='left')# }}}

def select_board(WIDTH, HEIGHT):# {{{
    print " WIDTH: " + str(WIDTH) + ", HEIGHT: " + str(HEIGHT)
    print "select WIDTH x HEIGHT (1: 5x4, 2: 6x5, 3: 7x6, ... 99: cancel, else:default(6x5) )"
    input_test_word = input(">>>  ")
    if input_test_word == 1:
        return (5, 4)
    elif input_test_word == 2:
        return (6, 5)
    elif input_test_word == 3:
        return (7, 6)
    elif input_test_word == 99:
        print "canceled changing board"
        return (WIDTH, HEIGHT)
    else:
        return (6, 5)# }}}

def show_parms(PARMS):# {{{
    print "show current parms ..."
    details = [# {{{
        'name',
        'red',
        'blue',
        'green',
        'light',
        'dark',
        'cure',
        '3colors',
        '4colors',
        '5colors',
        '3colors+cure',
        '4colors+cure',
        '5colors+cure',
        '4drops-red',
        '4drops-blue',
        '4drops-green',
        '4drops-light',
        '4drops-dark',
        '4drops-cure',
        '5drops-red',
        '5drops-blue',
        '5drops-green',
        '5drops-light',
        '5drops-dark',
        '5drops-cure',
        '1line-red',
        '1line-blue',
        '1line-green',
        '1line-light',
        '1line-dark',
        '1line-cure',
        ]# }}}
    for k in details:
        if PARMS.has_key(k):
            if isinstance(PARMS[k], float) and PARMS[k] != 0.0:
                print " " + str(k) + ": " + str(PARMS[k])
            elif isinstance(PARMS[k], str):
                print " " + str(k) + ": " + str(PARMS[k])# }}}

def select_parms_pattern(PARMS):# {{{
    print "current pattern name = " + PARMS['name']
    cnt = 0
    patterns = {}
    patterns_str = ""
    for k in PARMS_PATTERN.keys():
        patterns[cnt] = k
        patterns_str = patterns_str + str(cnt + 1) + ": " + k + ", "
        cnt += 1
    patterns_str = patterns_str + ", 98: show parm detail, 99: cancel"
    print "select parms pattern (" + patterns_str + ")"
    input_test_word = input(">>>  ")
    input_test_word -= 1
    if input_test_word == 98 - 1:
        show_parms(PARMS)
    elif input_test_word == 99 - 1:
        print "canceled changing parms"
    elif PARMS_PATTERN.has_key(patterns[input_test_word]):
        PARMS['name'] = patterns[input_test_word]
        print "changed pattern name = " + PARMS['name']
        for k in PARMS_PATTERN[patterns[input_test_word]].keys():
            if PARMS.has_key(k):
                PARMS[k] = PARMS_PATTERN[patterns[input_test_word]][k]
    return PARMS# }}}

def select_android_term(android_term):# {{{
    print "current android_term name = " + android_term
    print "select android_term (1: SC-03L(galaxy),  2: SHV32(aquos), ... else:default(galaxy s10) )"
    input_test_word = input(">>>  ")
    if input_test_word == 1:
        return "SC-03L"
    elif input_test_word == 2:
        return "SHV32"
    else:
        return "SC-03L"# }}}

if __name__ == '__main__':

    MAX_TURN, PLAYNUM, SWIPE = set_game_parms('default')
    #PARMS = DEFAULT_PARMS
    PARMS = {}
    PARMS['name'] = 'default'
    for k in PARMS_PATTERN['default'].keys():
        PARMS[k] = PARMS_PATTERN['default'][k]
    print "initail pattern name = " + PARMS['name']
    device_path = "/sdcard/screen.png"
    path = ".\screen.png"
    board = None
    android_term = ANDROID_TERM

    # main routine

    end_flg = True

    android_term = select_android_term(android_term)
    print " android_term: " + android_term

    while(end_flg):

        print "press key (1: get_ss, 2: search, 3: move,  4: get_ss & search, 5: search & move, "
        print "           6: get_ss & search & move, 7: select pattern, 8: change WIDTH & HEIGHT, "
        print "           9: select android_term,   99: exit )"
        input_test_word = input(">>>  ")
        if input_test_word == 1:
            board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 0, android_term)
        elif input_test_word == 2:
            board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1, android_term)
            n_best_route_xy = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, android_term)
        elif input_test_word == 3:
            moving_new(n_best_route_xy, key1, key2)
        if input_test_word == 4:
            board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 0, android_term)
            n_best_route_xy = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, android_term)
        elif input_test_word == 5:
            board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1, android_term)
            n_best_route_xy = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, android_term)
            moving_new(n_best_route_xy, key1, key2, android_term)
        elif input_test_word == 6:
            board, key1, key2 = getting_screenshot(device_path, path, WIDTH, HEIGHT, 0, android_term)
            n_best_route_xy = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, android_term)
            moving_new(n_best_route_xy, key1, key2, android_term)
        elif input_test_word == 7:
            PARMS = select_parms_pattern(PARMS)
        elif input_test_word == 8:
            WIDTH, HEIGHT = select_board(WIDTH, HEIGHT)
            print " WIDTH: " + str(WIDTH) + ", HEIGHT: " + str(HEIGHT)
        elif input_test_word == 9:
            android_term = select_android_term(android_term)
            print " android_term: " + android_term
        elif input_test_word == 99:
            print "pad_auto exit!!"
            end_flg = False
        else:
            print "press correct key!!"
            #end_flg = False

