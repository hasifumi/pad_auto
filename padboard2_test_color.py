# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard2
import pazdracombo
import time

#path = ".\screen_ojama.png"
path = ".\screen.png"
WIDTH = 6
HEIGHT = 5

start_time = time.time()

board = pazdracombo.convert_h_w_6x5(padboard2.check_board(path, WIDTH, HEIGHT, 0))
print "[4drops-check]"
print board
print ""
padboard2.print_board(WIDTH, HEIGHT, board)
print ""

elapsed_time = time.time() - start_time
print("searching time:{0}".format(elapsed_time)) + "[sec]"
