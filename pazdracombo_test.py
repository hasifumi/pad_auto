# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import padboard
import pazdracombo
import subprocess

width = 6
height = 5

PARMS = {# {{{
        'red'  : 1.0,
        'blue' : 1.0,
        'green': 1.0,
        'light': 1.0,
        'dark' : 1.0,
        'cure' : 1.0,
        '4colors'  : 1.0,
        '5colors'  : 0.0,
        '4colors+cure'  : 0.0,
        '5colors+cure'  : 0.0,
        '4drops-red'  : 0.0,
        '4drops-blue' : 1.0,
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

board = """
rrrrgg
bbbbcc
gbbggg
dddddd
crbbbb
""".replace('\n', '')
#board = "bdbbbddbdgdgbbbbbbggddddbdbbbg"

pdc = pazdracombo.PazdraComboChecker(width, height, board)
pdc.check_erasable(width, height)
pdc.calc_combo()
pdc.chk_drops4()
pdc.chk_drops5()
score, combo = pdc.calc_score(PARMS)

print "pdc.combo:" + str(pdc.combo)
print ""
print "pdc.combo_count:" + str(pdc.combo_count)
print ""
print "pdc.combo_seq:" + str(pdc.combo_seq)
print ""
print "pdc.combo_color:" + str(pdc.combo_color)
print ""
print "pdc.combo_color_count:" + str(pdc.combo_color_count)
print ""
print "pdc.combo_cure_count:" + str(pdc.combo_cure_count)
print ""
print "pdc.chk_1LineColor:" + str(pdc.chk_1LineColor())
print ""
print "pdc.chk_drops4:" + str(pdc.chk_drops4())
print ""
print "pdc.chk_drops5:" + str(pdc.chk_drops5())
print ""
print "pdc.score:" + str(score)
print ""
print "pdc.combo:" + str(combo)
print ""
#pdc.calc_score(parms)# }}}
#print pdc.combo
#print pdc.chk_drops4()

# width = 7
# height = 6
#
# board = """
# rrrrrrr
# bbbbbbb
# gbbgggg
# dddcddd
# ccccccc
# rrrrrrr
# """.replace('\n', '')
#
# pdc = pazdracombo.PazdraComboChecker(width, height, board)
#
# print pdc.adjacent
# print ""
# print pdc.renketsu_h
# print ""
# print pdc.renketsu_v
#
# print pdc.chk_drops_color()


