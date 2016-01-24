# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class SearchParms():

    SEARCH_PARMS_PATTERN = {# {{{
            'default' : {
                'MAX_TURN' : 35,
                'PLAYNUM'  : 25,
                },
            'win_tablet' : {
                'MAX_TURN' : 30,
                'PLAYNUM'  : 20,
                },
            'long_thinking' : {
                'MAX_TURN' : 50,
                'PLAYNUM'  : 50,
                },
            }# }}}

    def __init__(self, pattern_name='default'):# {{{
        self.set_search_parms(pattern_name)# }}}

    def show_search_parms(self):# {{{
        print "show search parms ... "
        for k, v in self.search_parms.iteritems():
            print " " + str(k) + ": " + str(v)# }}}

    def set_search_parms(self, pattern_name):# {{{
        if pattern_name in self.SEARCH_PARMS_PATTERN.keys():
            self.search_parms = {}
            self.search_parms["name"] = pattern_name
            for k, v in self.SEARCH_PARMS_PATTERN[pattern_name].iteritems():
                self.search_parms[k] = v
        return # }}}

    def get_search_parms_patttern(self):# {{{
        cnt = 0
        patterns = {}
        for k in self.SEARCH_PARMS_PATTERN.keys():
            patterns[cnt] = k
            cnt += 1
        return patterns# }}}

