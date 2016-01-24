# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_board

cols = 6
rows = 5
pic_path = ".\\screen.png"

pad_board = pad_board.Board(cols, rows, pic_path)

board = "012345678901234567890123456789"
print pad_board.convert_r_c(board)
