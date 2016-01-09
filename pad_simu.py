# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

WIDTH = 6# {{{
HEIGHT = 5# }}}

DEFAULT_GAME_PARMS = {# {{{
        'MAX_TURN' : 40,
        'PLAYNUM' : 30,
        'SWIPE' : 4,
        }# }}}

GAME_PARMS_PATTERN = {# {{{
        'default' : {
            'MAX_TURN' : 45,
            'PLAYNUM'  : 20,
            'SWIPE'    : 4,
            },
        'win_tablet' : {
            'MAX_TURN' : 30,
            'PLAYNUM'  : 25,
            'SWIPE'    : 5,
            },
        'long_thinking' : {
            'MAX_TURN' : 50,
            'PLAYNUM'  : 50,
            'SWIPE'    : 5,
            },
        'test1' : {
            'MAX_TURN' : 40,
            'PLAYNUM'  : 10,
            'SWIPE'    : 4,
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
            'red': 5.0,
            'light': 10.0,
            'cure': 5.0,
            '4drops-red' : 5.0,
            '4drops-blue': 3.0,
            '4drops-light' : 10.0,
            '4drops-dark': 3.0,
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
        'basteto/shiva': {
            'red': 10.0,
            'green': 10.0,
            'cure': 5.0,
            '4drops-red': 50.0,
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
        }# }}}

import padboard
#import uiautomator
import time
import subprocess
import os
import pad_search
#import pazdracombo
#from PIL import Image
import random

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}

def searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS):# {{{
    # if board is None:
    #     board = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1)  # すでに取得済みのscreenshotを利用する
    print "searching ..."
    start_time = time.time()
    n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    # pos_x, pos_y = get_route(n_best.route, is_nexus(path), WIDTH)
    # # 確認用
    # print "[board]"
    # print print_board(WIDTH, HEIGHT, board)
    # print ""
    # print "[combo]"
    # print print_board(WIDTH, HEIGHT, n_best.board)
    # print ""
    elapsed_time = time.time() - start_time
    return (n_best, elapsed_time)# }}}

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

DROP = {# {{{
        '0': 'r',
        '1': 'b',
        '2': 'g',
        '3': 'l',
        '4': 'd',
        '5': 'c',
        }# }}}

def make_random_drop(WIDTH, HEIGHT, DROP):# {{{
    board = ""
    for i in range(WIDTH * HEIGHT):
        board += DROP[str(random.randint(0,5))]
        # d = random.randint(0,5)
        # print d
        # board += DROP[str(d)]
    return board# }}}

if __name__ == '__main__':

    MAX_TURN, PLAYNUM, SWIPE = set_game_parms('default')
    PARMS = {}
    PARMS['name'] = 'default'
    for k in PARMS_PATTERN['default'].keys():
        PARMS[k] = PARMS_PATTERN['default'][k]
    print "initail pattern name = " + PARMS['name']
    print ""
    #device_path = "/sdcard/screen.png"
    #path = ".\screen.png"
    board = None

    simu_times = 5
    scores = 0
    combos = 0
    total_elapsed_time = 0

    # main routine

    print "pad_simu started " + " (" + str(simu_times) + " times) ..."
    print ""

    # board = make_random_drop(WIDTH, HEIGHT, DROP)
    # print " board: " + str(board)

    for i in range(simu_times):
        board = make_random_drop(WIDTH, HEIGHT, DROP)
        print "time " + str(i+1) + " : " + ",  board: " + str(board)
        n_best, elapsed_time = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
        scores += n_best.score
        combos += n_best.combo
        total_elapsed_time += elapsed_time
        print "time " + str(i+1) + " : " + ",  score: " + str(n_best.score)
        print "time " + str(i+1) + " : " + ",  combo: " + str(n_best.combo)
        print "time " + str(i+1) + " : " + ",  elapsed_time: {0}".format(elapsed_time) + "[sec]"
        print ""

    show_game_parms()
    print("avarage score:{0}".format(str(scores/simu_times))) + "[point]"
    print("avarage combo:{0}".format(str(combos/simu_times))) + "[combo]"
    print("avarage time:{0}".format(total_elapsed_time/simu_times)) + "[sec]"


