# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

import numpy
from PIL import Image
import multiprocessing as mp

pic_parm = {
        '405': {    # SH-01F by vnc & pyws
            '5x4': {# {{{
                'xa': 10,
                'ya': 355,
                'xb': 90,
                'yb': 435,
                'xs': 80,
                'ys': 80,
            },# }}}
            '6x5': {# {{{
                'xa': 10,
                'ya': 350,
                'xb': 75,
                'yb': 415,
                'xs': 65,
                'ys': 65,
            },# }}}
            '7x6': {# {{{
                'xa': 15,
                'ya': 350,
                'xb': 70,
                'yb': 405,
                'xs': 55,
                'ys': 55,
            },# }}}
        },
        '600': {    # Nexus7(2012) by vnc & pyws
            '5x4': {# {{{
                'xa': 15,
                'ya': 460,
                'xb': 130,
                'yb': 575,
                'xs': 115,
                'ys': 115,
            },# }}}
            '6x5': {# {{{
                'xa': 15,
                'ya': 455,
                'xb': 110,
                'yb': 550,
                'xs': 95,
                'ys': 95,
            },# }}}
            '7x6': {# {{{
                'xa': 25,
                'ya': 455,
                'xb': 105,
                'yb': 535,
                'xs': 80,
                'ys': 80,
            },# }}}
        },
        '800': {    # Nexus7(2012)
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
        '1080': {   # SH-01F
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

def get_rgb(pic, box=""):# {{{
    if box == "":
        #box = (0, 0, pic.width, pic.height)
        box = (0, 0, pic.size[0], pic.size[1])
    #print "box: " + str(box)
    rgbimg = pic.crop(box).convert("RGB")
    rgb = numpy.array(rgbimg.getdata())
    return [__round(rgb[:,0]),
            __round(rgb[:,1]),
            __round(rgb[:,2])]# }}}

def color(array, flg=1):# {{{
    col = {}
    if flg == 0:
        col["r"] = [205, 110, 130]
        col["b"] = [100, 140, 190]
        col["g"] = [100, 160, 120]
        col["l"] = [200, 175, 110]
        col["d"] = [165, 90,  170]
        col["c"] = [200, 100, 150]
        col["o"] = [45,  45,  55]     # ojama
        col["p"] = [120, 95,  115]    # poison
    else:
        col["1"] = [205, 110, 130]
        col["2"] = [100, 140, 190]
        col["3"] = [100, 160, 120]
        col["4"] = [200, 175, 110]
        col["5"] = [165, 90, 170]
        col["6"] = [200, 100, 150]
        col["7"] = [45,  45,  55]     # ojama
        col["8"] = [120, 95,  115]    # poison

    max = 0
    result = ""
    for k, c in col.items():
       tmp = numpy.corrcoef(numpy.array(array), numpy.array(c))[0][1]
       if max < tmp:
           result = k
           max = tmp
    return result# }}}

def __round(array):# {{{
    return int(round(numpy.average(array)))# }}}

def wrap_func(args):# {{{
    return args[0](*args[1:])# }}}

def get_rows_rgb(rows, edges, pic, i, flg):# {{{
    rows_rgb = ""
    for j in range(rows):
        box = (edges['xa'] + edges['xs']*i,
               edges['ya'] + edges['ys']*j,
               edges['xb'] + edges['xs']*i,
               edges['yb'] + edges['ys']*j)
        rgb = get_rgb(pic, box)
        #print "rgb: " + str(rgb)
        rows_rgb += color(rgb, flg)
    return rows_rgb# }}}

def check_board(path, cols, rows, flg=1):# {{{
    pic = Image.open(path, 'r')

    #key1 = str(pic.width)
    key1 = str(pic.size[0])
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
        if pic_parm[key1].has_key(key2):
            for k in edges.keys():
                edges[k] = pic_parm[key1][key2][k]

    board = ""
    for i in range(cols):
        rows_rgb = get_rows_rgb(rows, edges, pic, i, flg)
        board += rows_rgb

    return board# }}}

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}

