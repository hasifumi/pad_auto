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
        'MAX_TURN' : 40,
        'PLAYNUM' : 30,
        'SWIPE' : 4,
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
            'ble': 5.0,
            '3colors': 10.0,
            '5colors+cure': 20.0,
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

#import padboard
#import uiautomator
import time
import subprocess
import os
import pad_search
import pazdracombo
#from PIL import Image
import sys

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

def is_nexus(path):# {{{
    pic = Image.open(path, 'r')
    #if pic.width == 800:
    if pic.size[0] == 800:
        return True
    else:
        return False# }}}

def is_nexus2(width):# {{{
    if width == 800:
        return True
    else:
        return False# }}}

def idx2xy(width, idx):# {{{
    return[int(idx/width), int(idx%width)]# }}}

def conv_x(i, is_nexus2, width=6):# {{{
    if is_nexus2:
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

def conv_y(i, is_nexus2, width=6):# {{{
    if is_nexus2:
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

def calc_i(flag, ary, is_nexus2, width):# {{{
    pos_i = "\""
    for i,v in enumerate(ary):
        if flag == "x":
            pos_i += str(conv_x(ary[i], is_nexus2, width))
        else:
            pos_i += str(conv_y(ary[i], is_nexus2, width))
        pos_i += ","
    pos_i = pos_i.rstrip(",")
    pos_i += "\""
    return pos_i# }}}

def get_route(route, is_nexus2, width):# {{{
    #print "get_route width:" + str(width)
    x = []
    y = []
    #print "route:" + str(route)
    for r in route:
        #print "r:" + r
        ans = idx2xy(WIDTH, int(r))
        x.append(ans[1])
        y.append(ans[0])
    pos_x = calc_i("x", x, is_nexus2, width)
    pos_y = calc_i("y", y, is_nexus2, width)
    return (pos_x, pos_y)# }}}

def move_drop(pos_x, pos_y, swipe_time):# {{{
    uiautomator_cmd = ["adb", "shell", "uiautomator", "runtest", "UiAutomator.jar", "-c", "com.hahahassy.android.UiAutomator#swipe", "-e",  "\"x\"", pos_x, "-e","\"y\"", pos_y, "-e","\"t\"", swipe_time]
    subprocess.check_call(uiautomator_cmd, shell=True)# }}}

def getting_screenshot(device_path, path, WIDTH, HEIGHT, use_old=0):# {{{
    if use_old == 0:
        print "getting screenshot ..."
        start_time = time.time()
        get_screenshot(device_path)
    else:
        print "using old screenshot ..."
        start_time = time.time()

    elapsed_time = time.time() - start_time
    print("getting time:{0}".format(elapsed_time)) + "[sec]"

    print "checking board ..."
    start_time = time.time()
    cmd = ["python", "padboard2.py", path, str(WIDTH), str(HEIGHT)]
    #print "cmd:" + str(cmd)
    p = subprocess.check_output(cmd)
    #print "p:" + str(p)
    sout = p.rstrip().split(",")
    if WIDTH == 5:
        board = pazdracombo.convert_h_w_5x4(sout[0])
    elif WIDTH == 6:
        board = pazdracombo.convert_h_w_6x5(sout[0])
    elif WIDTH == 7:
        board = pazdracombo.convert_h_w_7x6(sout[0])
    elapsed_time = time.time() - start_time
    print("checking time:{0}".format(elapsed_time)) + "[sec]"
    #print "board:" + str(board) + " , sout[1]:" + str(sout[1])
    return board, sout[1]# }}}

def searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width):# {{{
    if board is None:
        board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1)  # すでに取得済みのscreenshotを利用する
    print "[board]"
    print print_board(WIDTH, HEIGHT, board)
    print ""

    print "searching ..."
    start_time = time.time()
    n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    #cmd = ["pypy", "pad_search.py", str(WIDTH), str(HEIGHT), board, str(MAX_TURN), str(PLAYNUM), "isis"]
    #print "cmd:" + str(cmd)
    #p = subprocess.check_output(cmd)
    #print "p(n_best.route):" + str(p)
    #sout = p.rstrip().split(",")
    #sout_route = []
    #for i in sout:
    #    sout_route.append(i)
    pos_x, pos_y = get_route(n_best.route, is_nexus2(pic_width), WIDTH)
    #pos_x, pos_y = get_route(sout_route, is_nexus2(pic_width), WIDTH)
    # 確認用
    # print "[board]"
    # print print_board(WIDTH, HEIGHT, board)
    # print ""
    # print "[combo]"
    # print print_board(WIDTH, HEIGHT, n_best.board)
    # print ""
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


if __name__ == '__main__':

    MAX_TURN, PLAYNUM, SWIPE = set_game_parms('default')
    #PARMS = DEFAULT_PARMS
    PARMS = {}
    PARMS['name'] = 'default'
    for k in PARMS_PATTERN['default'].keys():
        PARMS[k] = PARMS_PATTERN['default'][k]
    print "initail pattern name = " + PARMS['name']
    device_path = "/sdcard/screen.png"
    #path = ".\screen.png"
    path = "screen.png"
    board = None
    pic_width = 0

    # main routine

    end_flg = True

    while(end_flg):

        print "press key (1: get_ss, 2: search, 3: move,  4: get_ss & search, 5: search & move, "
        print "           6: get_ss & search & move, 7: select pattern, 8: change WIDTH & HEIGHT, 99: exit )"
        input_test_word = input(">>>  ")
        if input_test_word == 1:
            board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT)
        elif input_test_word == 2:
            pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width)
        elif input_test_word == 3:
            moving(pos_x, pos_y, SWIPE)
        elif input_test_word == 4:
            board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT)
            pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width)
        elif input_test_word == 5:
            pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width)
            moving(pos_x, pos_y, SWIPE)
        elif input_test_word == 6:
            #board = getting_screenshot(device_path, path, WIDTH, HEIGHT)
            board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT)
            pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width)
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

