# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

import numpy
from PIL import Image
import multiprocessing as m
import padboard

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

def get_rgb(pic, box=""):# {{{
    if box == "":
        box = (0, 0, pic.width, pic.height)
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
        col["d"] = [165, 90, 170]
        col["c"] = [200, 100, 150]
        #col["o"] = [40, 75, 100]    # ojama
        #col["o"] = [225, 200, 130]    # ojama
        #col["p"] = [250, 250, 245]    # poison
    else:
        col["1"] = [205, 110, 130]
        col["2"] = [100, 140, 190]
        col["3"] = [100, 160, 120]
        col["4"] = [200, 175, 110]
        col["5"] = [165, 90, 170]
        col["6"] = [200, 100, 150]
        #col["7"] = [85, 115, 130]    # ojama
        #col["7"] = [225, 200, 130]    # ojama
        #col["8"] = [250, 250, 245]    # poison

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

def wrap_get_rgb_rows(args):# {{{
    """ wrapper func """
    print "wrap"
    return args[0](*args[1:])# }}}

def get_rgb_rows(pic, rows, edges, i, flg):# {{{
    print "get_rgb_rows"
    clr = ""
    for j in range(rows):
        box = (edges['xa'] + edges['xs']*i,
               edges['ya'] + edges['ys']*j,
               edges['xb'] + edges['xs']*i,
               edges['yb'] + edges['ys']*j)
        rgb = get_rgb(pic, box)
        clr = clr + color(rgb, flg)
    return clr # }}}

def check_board(path, cols, rows, flg=1):# {{{
    pic = Image.open(path, 'r')

    key1 = str(pic.width)
    key2 = str(cols)+"x"+str(rows)
    edges = {# {{{
            'xa': 0,
            'ya': 0,
            'xb': 0,
            'yb': 0,
            'xs': 0,
            'ys': 0,
        }# }}}

    if pic_parm.has_key(key1):
        if pic_parm[key1].has_key(key2):
            for k in edges.keys():
                edges[k] = pic_parm[key1][key2][k]

    board = ""
    for i in range(cols):
        print " cpu_count : " + str(m.cpu_count())
        p = m.Pool()
        func_args = []
        for r in range(rows):
            func_args.append((get_rgb_rows, pic, r, edges, i, flg))
        print " func_args: " + str(func_args)
        board = board + p.map(wrap_get_rgb_rows, func_args)

        #board = board + get_rgb_rows(pic, rows, edges, i, flg)

        #for j in range(rows):
        #    box = (edges['xa'] + edges['xs']*i,
        #           edges['ya'] + edges['ys']*j,
        #           edges['xb'] + edges['xs']*i,
        #           edges['yb'] + edges['ys']*j)
        #    rgb = get_rgb(pic, box)
        #    board = board + color(rgb, flg)
    return board# }}}

def print_board(width, height, board):# {{{
    for h in range(height):
        print board[h*width:h*width+width]
    return 1# }}}


path = ".\screen_sh-01f_5x4.png"
WIDTH = 5
HEIGHT = 4

temp_board = padboard.check_board(path, WIDTH, HEIGHT)
board = pazdracombo.convert_h_w_5x4(temp_board)
print "[4drops-check]"
print board
print ""
padboard.print_board(WIDTH, HEIGHT, board)
print ""
