# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_combo

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

pad_game_parms = pad_game_parms.GameParms()
pad_score_parms = pad_score_parms.ScoreParms()
pad_search_parms = pad_search_parms.SearchParms()

pad_searcher = pad_searcher.Searcher(pad_game_parms, pad_score_parms, pad_search_parms, board)

pad_combo = pad_combo.PadCombo(pad_searcher.game_parms.width, \
                               pad_searcher.game_parms.height, \
                               pad_searcher.board, \
                               pad_searcher.score_parms)

print "board_l: " + str(pad_combo.board_l)
print "adjacent: " + str(pad_combo.adjacent)
print "renketsu_h: " + str(pad_combo.renketsu_h)
print "renketsu_v: " + str(pad_combo.renketsu_v)
print ""

pad_combo.check_erasable()
pad_combo.calc_combo()
print "combo_count: " + str(pad_combo.combo_count)
print "combo_seq: " + str(pad_combo.combo_seq)
print "combo_color: " + str(pad_combo.combo_color)
print "combo_color_count: " + str(pad_combo.combo_color_count)
print "combo_cure_count: " + str(pad_combo.combo_cure_count)
print ""

print pad_searcher.score_parms
print pad_combo.calc_score(pad_searcher.score_parms)


print "** board **"
print pad_combo.print_lst2str("board")
print ""
print "** erase **"
print pad_combo.print_lst2str("erase")
print ""
print "** erase2 **"
print pad_combo.print_lst2str("erase2")
print ""


