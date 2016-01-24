# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import os
import sys
import time
import subprocess

import pad_game_parms
import pad_score_parms
import pad_search_parms
import pad_board
import pad_combo
import pad_searcher

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}

def get_screenshot(device_path):# {{{
    screencap_cmd = ["adb", "shell", "screencap", device_path]
    subprocess.check_call(screencap_cmd, shell=True)

    pull_cmd = ["adb", "pull", device_path]
    subprocess.check_call(pull_cmd, shell=True)

    return# }}}

def is_nexus(pic_width):# {{{
    if pic_width == 800:
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
    cmd = ["python", "pad_board.py", path, str(WIDTH), str(HEIGHT)]
    p = subprocess.check_output(cmd)
    sout = p.rstrip().split(",")
    #if WIDTH == 5:
    #    board = pazdracombo.convert_h_w_5x4(sout[0])
    #elif WIDTH == 6:
    #    board = pazdracombo.convert_h_w_6x5(sout[0])
    #elif WIDTH == 7:
    #    board = pazdracombo.convert_h_w_7x6(sout[0])
    elapsed_time = time.time() - start_time
    print("checking time:{0}".format(elapsed_time)) + "[sec]"
    return board, sout[1]# }}}

def searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width):# {{{
    if board is None:
        board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT, 1)  # すでに取得済みのscreenshotを利用する
    print "searching ..."
    start_time = time.time()
    n_best = pad_search.Nbeam(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS)
    pos_x, pos_y = get_route(n_best.route, is_nexus(pic_width), WIDTH)
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
        return (7, 6)
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

    device_path = "/sdcard/screen.png"
    path = "screen.png"
    board = None
    pic_width = 0

    game_parms = pad_game_parms.GameParms()
    game_parms.show_game_parms()

    score_parms = pad_score_parms.ScoreParms()
    score_parms.show_score_parms()

    # main routine

    end_flg = True

    while(end_flg):

        print "press key (1: get_ss, 2: search, 3: move,  4: get_ss & search, 5: search & move, "
        print "           6: get_ss & search & move, 7: select pattern, 8: change WIDTH & HEIGHT, 99: exit )"
        input_test_word = input(">>>  ")
        if input_test_word == 1:
            #board, pic_width = getting_screenshot(device_path, path, WIDTH, HEIGHT)
            board, pic_width = getting_screenshot(device_path, path, game_parms.width, game_parms.height)
        elif input_test_word == 2:
            #pos_x, pos_y = searching(WIDTH, HEIGHT, board, MAX_TURN, PLAYNUM, PARMS, pic_width)
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

