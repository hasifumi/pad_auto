# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo
import subprocess

width = 6
height = 5

board = """
rrrrrr
bbbbbb
gbbggg
dddcdd
cccccc
""".replace('\n', '')
#board = "bdbbbddbdgdgbbbbbbggddddbdbbbg"

width = 7
height = 6

board = """
rrrrrrr
bbbbbbb
gbbgggg
dddcddd
ccccccc
rrrrrrr
""".replace('\n', '')

pdc = pazdracombo.PazdraComboChecker(width, height, board)

print pdc.adjacent
print ""
print pdc.renketsu_h
print ""
print pdc.renketsu_v


