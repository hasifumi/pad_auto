# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_game_parms

game_parms = pad_game_parms.GameParms()

game_parms.show_game_parms()

print game_parms.get_board_pattern()

game_parms.set_board_parms("5x4")
game_parms.set_swipe(3)
game_parms.show_game_parms()
