# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class GameParms():

    BOARD_PATTERN = {# {{{
            '5x4' : {# {{{
                "width" : 5,
                "height": 4,
                },# }}}
            '6x5' : {# {{{
                "width" : 6,
                "height": 5,
                },# }}}
            '7x6' : {# {{{
                "width" : 7,
                "height": 6,
                },# }}}
            }# }}}

    def __init__(self, board_pattern_name="6x5", swipe=4):# {{{
        self.width = 0
        self.height = 0
        self.set_board_parms(board_pattern_name)
        self.set_swipe(swipe)
        return # }}}

    def show_game_parms(self):# {{{
        print "show game parms ... "
        print " width: " + str(self.width)
        print " height:" + str(self.height)
        print " swipe: " + str(self.swipe)
        return # }}}

    def set_board_parms(self, pattern_name):# {{{
        if pattern_name in self.BOARD_PATTERN.keys():
            for k, v in self.BOARD_PATTERN[pattern_name].iteritems():
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
        return # }}}

    def get_board_pattern(self):# {{{
        cnt = 0
        patterns = {}
        for k in self.BOARD_PATTERN.keys():
            patterns[cnt] = k
            cnt += 1
        return patterns# }}}

    def set_swipe(self, SWIPE):# {{{
        self.swipe = SWIPE# }}}
