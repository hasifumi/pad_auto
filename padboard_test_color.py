# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo

#path = ".\screen_ojama.png"
path = ".\screen.png"
WIDTH = 6
HEIGHT = 5

board = pazdracombo.convert_h_w_6x5(padboard.check_board(path, WIDTH, HEIGHT, 0))
print "[4drops-check]"
print board
print ""
padboard.print_board(WIDTH, HEIGHT, board)
print ""

