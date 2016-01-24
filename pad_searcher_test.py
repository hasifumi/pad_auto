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

pad_searcher = pad_searcher.Searcher(pad_game_parms, pad_score_parms, pad_search_parms, board)

print pad_searcher.adjacent

x = 1
y = 3
print "x: " + str(x) + ", y: " + str(y)
print "xy2idx: " + str(pad_searcher.xy2idx(x, y))

print "get_adjacent(19): " + str(pad_searcher.get_adjacent(19))
print "get_adjacent(25): " + str(pad_searcher.get_adjacent(25))

print "swap(1, 2, board)before:" + str(board)
print "swap(1, 2, board)after :" + str(pad_searcher.swap(1, 2, board))

print pad_searcher.calc_score(pad_searcher.board)

#print pad_searcher.search_node_array(0)

print pad_searcher.beam_search()
