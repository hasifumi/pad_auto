# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class ScoreParms():

    SCORE_PARMS_PATTERN = {# {{{
            'default': {# {{{
                'red'  : 0.0,
                'blue' : 0.0,
                'green': 0.0,
                'light': 0.0,
                'dark' : 0.0,
                'cure' : 0.0,
                '3colors'  : 0.0,
                '4colors'  : 0.0,
                '5colors'  : 0.0,
                '3colors+cure'  : 0.0,
                '4colors+cure'  : 0.0,
                '5colors+cure'  : 0.0,
                '4drops-red'  : 0.0,
                '4drops-blue' : 0.0,
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
                },# }}}
            'saria, tall': {# {{{
                'red': 2.0,
                'green': 3.0,
                'light': 3.0,
                'cure': 5.0,
                '4drops-red' : 5.0,
                '4drops-blue': 3.0,
                '4drops-green': 5.0,
                '4drops-light' : 10.0,
                '5drops-red' : -5.0,
                '5drops-green' : -10.0,
                '5drops-light' : -10.0,
                '1line-red': 10.0,
                '1line-light': 30.0,
                },# }}}
            'blue-sonia, ryune': {# {{{
                'blue': 10.0,
                'dark': 5.0,
                'cure': 5.0,
                '4drops-blue': 10.0,
                '4drops-light' : 5.0,
                '4drops-dark' : 5.0,
                '5drops-blue': 50.0,
                '1line-blue': 50.0,
                '1line-dark': 10.0,
                },# }}}
            'basteto/shiva': {# {{{
                'red': 10.0,
                'green': 10.0,
                'cure': 5.0,
                '4drops-red': 50.0,
                '4drops-blue': 50.0,
                '4drops-green': 50.0,
                '1line-red': -10.0,
                '1line-green': -10.0,
                },# }}}
            'athena': {# {{{
                'light': 10.0,
                'green': 5.0,
                'cure': 5.0,
                '4drops-green': 10.0,
                '4drops-light': 30.0,
                },# }}}
            'zeroge-4drops': {# {{{
                'dark': 30.0,
                'blue': 10.0,
                'cure': 10.0,
                '4drops-dark': 20.0,
                '1line-dark': -10.0,
                },# }}}
            'zeroge': {# {{{
                'dark': 30.0,
                'blue': 10.0,
                'cure': 10.0,
                '1line-dark': -10.0,
                },# }}}
            'isis': {# {{{
                '3colors': 10.0,
                },# }}}
            'izuizu, ryune': {# {{{
                'dark': 5.0,
                'blue': 15.0,
                'cure': 10.0,
                '4drops-blue': 20.0,
                '4drops-dark': 10.0,
                '1line-blue': -10.0,
                '1line-dark': -10.0,
                },# }}}
            'horus': {# {{{
                'cure': 5.0,
                '4colors'  : 10.0,
                '5colors'  : 5.0,
                '3colors+cure'  : 5.0,
                '4colors+cure'  : 5.0,
                '5colors+cure'  : 5.0,
                },# }}}
            'awaken lucifer': {# {{{
                'cure': 5.0,
                '4drops-blue': 5.0,
                '4drops-dark': 10.0,
                '1line-dark':  20.0,
                },# }}}
            }# }}}

    def __init__(self, pattern_name='default'):# {{{
        self.set_score_parms(pattern_name)# }}}

    def show_score_parms(self):# {{{
        print "show score parms ... "
        print " name: " + str(self.score_parms["name"])
        for k in self.SCORE_PARMS_PATTERN['default'].keys():
            if self.score_parms.has_key(k):
                if isinstance(self.score_parms[k], float) and self.score_parms[k] != 0.0:
                    print " " + str(k) + ": " + str(self.score_parms[k])# }}}

    def set_score_parms(self, pattern_name):# {{{
        if pattern_name in self.SCORE_PARMS_PATTERN.keys():
            self.score_parms = {}
            self.score_parms["name"] = pattern_name
            for k, v in self.SCORE_PARMS_PATTERN[pattern_name].iteritems():
                self.score_parms[k] = v
        return # }}}

    def get_score_parms_patttern(self):# {{{
        cnt = 0
        patterns = {}
        for k in self.SCORE_PARMS_PATTERN.keys():
            patterns[cnt] = k
            cnt += 1
        return patterns# }}}
