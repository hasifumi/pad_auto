# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_game_parms
import pad_score_parms
import pad_search_parms
import pad_searcher

board = """
ddcccd
cddddd
dddddd
dccddc
cddddd
""".replace('\n', '')

#def __init__(self, game_parms, score_parms, search_parms, board):
pad_game_parms = pad_game_parms.GameParms()
pad_score_parms = pad_score_parms.ScoreParms()
pad_search_parms = pad_search_parms.SearchParms()

searcher = pad_searcher.Searcher(pad_game_parms, pad_score_parms, pad_search_parms, board)

print searcher.adjacent

x = 1
y = 3
print "x: " + str(x) + ", y: " + str(y)
print "xy2idx: " + str(searcher.xy2idx(x, y))

print "get_adjacent(19): " + str(searcher.get_adjacent(19))
print "get_adjacent(25): " + str(searcher.get_adjacent(25))

print "swap(1, 2, board)before:" + str(board)
print "swap(1, 2, board)after :" + str(searcher.swap(1, 2, board))

print searcher.calc_score(searcher.board)

#print searcher.search_node_array(0)

print searcher.beam_search()
