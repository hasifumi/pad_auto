# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo
import subprocess

width = 6
height = 5

PARMS = {# {{{
        'red'  : 0.0,
        'blue' : 0.0,
        'green': 0.0,
        'light': 1.0,
        'dark' : 0.0,
        'cure' : 1.0,
        '3colors'  : 0.0,
        '4colors'  : 4.0,
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
        '1line-red'  : 1.0,
        '1line-blue' : 0.0,
        '1line-green': 0.0,
        '1line-light': 0.0,
        '1line-dark' : 0.0,
        '1line-cure' : 0.0,
        }# }}}

#board = """
#rrrrrr
#bbbbbb
#gbbggg
#dddcdd
#cccccc
#""".replace('\n', '')
board = "bdbbbddbdgdgbbbbbbggddddbdbbbg"

pdc = pazdracombo.PazdraComboChecker(width, height, board)

#screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
#subprocess.check_call(screencap_cmd, shell=True)
#
#pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
#subprocess.check_call(pull_cmd, shell=True)

#board = padboard.check_board(".\screen.png", 6, 5, 0)
#print board
#board2 = pazdracombo.convert_h_w(board)
#print board2
#
#pdc = pazdracombo.PazdraComboChecker(width, height, board2)

# 確認用
print "[board]"
print pdc.print_lst2str("board")

pdc.check_erasable()
pdc.calc_combo()

## 確認用
print "[combo]"
print pdc.print_combo()
score, combo = pdc.calc_score(PARMS)
print "score: " + str(score) + ", combo: " + str(combo)

print pdc.combo

color = pdc.chk1LineColor()
print color

