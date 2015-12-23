# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo

path = ".\screen_sh-01f_5x4.png"
WIDTH = 5
HEIGHT = 4
answer_5x4 = "dbdcbbddcrldrgllrcbc"

board = pazdracombo.convert_h_w_5x4(padboard.check_board(path, WIDTH, HEIGHT, 0))
print "[5x4]"
print board
if board == answer_5x4:
    print "correct!"
else:
    print "wrong!!"
padboard.print_board(WIDTH, HEIGHT, board)
print ""

path = ".\screen_sh-01f_6x5.png"
WIDTH = 6
HEIGHT = 5
answer_6x5 = "rlrbbgrbcrgrdgddgcllcrdrbgbldg"

board = pazdracombo.convert_h_w_6x5(padboard.check_board(path, WIDTH, HEIGHT, 0))
print "[6x5]"
print board
if board == answer_6x5:
    print "correct!"
else:
    print "wrong!!"
padboard.print_board(WIDTH, HEIGHT, board)
print ""

path = ".\screen_sh-01f_7x6.png"
WIDTH = 7
HEIGHT = 6
answer_7x6 = "cdgrlbrllbldldrbbdrgcbllddbclgbgbglggcgrbl"

board = pazdracombo.convert_h_w_7x6(padboard.check_board(path, WIDTH, HEIGHT, 0))
print "[7x6]"
print board
if board == answer_7x6:
    print "correct!"
else:
    print "wrong!!"
padboard.print_board(WIDTH, HEIGHT, board)
print ""

# answer
#
# [5x4]
# dbdcb
# bddcr
# ldrgl
# lrcbc
# [6x5]
# rlrbbg
# rbcrgr
# dgddgc
# llcrdr
# bgbldg
# [7x6]
# cdgrlbr
# llbldld
# rbbdrgc
# bllddbc
# lgbgbgl
# ggcgrbl
