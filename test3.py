# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

# import pad_parm
#
# parms = pad_parm.padParm()
#
# print parms.game_parms
# print parms.score_parms

pic_parm = {
        '800': {   # Nexus7(2012)
            '5x4': {# {{{
                'xa': 15,
                'ya': 575,
                'xb': 170,
                'yb': 730,
                'xs': 155,
                'ys': 155,
            },# }}}
            '6x5': {# {{{
                'xa': 15,
                'ya': 560,
                'xb': 145,
                'yb': 690,
                'xs': 130,
                'ys': 130,
            },# }}}
        },
        '1080': {  # SH-01F
            '5x4': {# {{{
                'xa': 5,
                'ya': 865,
                'xb': 215,
                'yb': 1075,
                'xs': 210,
                'ys': 210,
            },# }}}
            '6x5': {# {{{
                'xa': 5,
                'ya': 860,
                'xb': 185,
                'yb': 1030,
                'xs': 180,
                'ys': 180,
            },# }}}
            '7x6': {# {{{
                'xa': 25,
                'ya': 850,
                'xb': 170,
                'yb': 995,
                'xs': 145,
                'ys': 145,
            },# }}}
        },
    }

width = 1080
cols = 7
rows = 6
key1 = str(width)
key2 = str(cols)+"x"+str(rows)
edges = {
        'xa': 0,
        'ya': 0,
        'xb': 0,
        'yb': 0,
        'xs': 0,
        'ys': 0,
    }

if pic_parm.has_key(key1):
    print "has " + key1
    if pic_parm[key1].has_key(key2):
        for k in edges.keys():
            edges[k] = pic_parm[key1][key2][k]
            print "edges[k]: " + str(edges[k])
    #if parm.has_key(str(cols)+"x"+str(rows)):
