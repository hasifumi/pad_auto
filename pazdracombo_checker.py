# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo
import subprocess

width = 6
height = 5
#board = "rddbgbrrrbgbrlgbgbglglllclgbbl"
board = "rddbgbrrrbgbrlllgbgggbbbclglll"
board = "rddbgbrrlbgbrlgbgbglgrbbclglll"

pdc = pazdracombo.PazdraComboChecker(width, height, board)

#screencap_cmd = ["adb", "shell", "screencap", "/sdcard/screen.png"]
#subprocess.check_call(screencap_cmd, shell=True)
#
#pull_cmd = ["adb", "pull", "/sdcard/screen.png"]
#subprocess.check_call(pull_cmd, shell=True)
#
#board = padboard.check_board(".\screen.png", 6, 5, 0)
#print board
#board2 = pazdracombo.convert_h_w(board)
#print board2

# 確認用
print "[board]"
print pdc.print_lst2str("board")

pdc.check_erasable()
pdc.calc_combo()

## 確認用
print "[combo]"
print "sum_combo(): " + str(pdc.sum_combo())
print pdc.calc_score(light=5, red=2)
pdc.print_combo()
#print pdc.combo

