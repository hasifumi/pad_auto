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
#        '1080': {   # SH-01F
#            '5x4': {# {{{
#                'xa': 5,
#                'ya': 865,
#                'xb': 215,
#                'yb': 1075,
#                'xs': 210,
#                'ys': 210,
#            },# }}}
#            '6x5': {# {{{
#                'xa': 5,
#                'ya': 860,
#                'xb': 185,
#                'yb': 1030,
#                'xs': 180,
#                'ys': 180,
#            },# }}}
#            '7x6': {# {{{
#                'xa': 25,
#                'ya': 850,
#                'xb': 170,
#                'yb': 995,
#                'xs': 145,
#                'ys': 145,
#            },# }}}
#        },
        '1080': {   # Galaxy S10
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
                'ya': 1370,
                'xb': 185,
                'yb': 1550,
                'xs': 180,
                'ys': 180,
            },# }}}
        },
        '392': {   # Galaxy S10 by scrcpy
            '6x5': {# {{{
                'xa': 10,
                'ya': 510,
                'xb': 70,
                'yb': 570,
                'xs': 60,
                'ys': 60,
            },# }}}
            '7x6': {# {{{
                'xa': 15,
                'ya': 510,
                'xb': 65,
                'yb': 565,
                'xs': 50,
                'ys': 50,
            },# }}}
        },
        '464': {   # AQUOS SHV32 by scrcpy
            '5x4': {# {{{
                'xa': 30,
                'ya': 440,
                'xb': 110,
                'yb': 520,
                'xs': 80,
                'ys': 80,
            },# }}}
            '6x5': {# {{{
                'xa': 30,
                'ya': 430,
                'xb': 100,
                'yb': 500,
                'xs': 70,
                'ys': 70,
            },# }}}
            '7x6': {# {{{
                'xa': 35,
                'ya': 430,
                'xb': 95,
                'yb': 490,
                'xs': 60,
                'ys': 60,
            },# }}}
        },
        '520': {   # Kindle FireHD8 by scrcpy
            '5x4': {# {{{
                'xa': 30,
                'ya': 440,
                'xb': 110,
                'yb': 520,
                'xs': 80,
                'ys': 80,
            },# }}}
            '6x5': {# {{{
                'xa': 45,
                'ya': 435,
                'xb': 115,
                'yb': 505,
                'xs': 70,
                'ys': 70,
            },# }}}
            '7x6': {# {{{
                'xa': 50,
                'ya': 435,
                'xb': 110,
                'yb': 495,
                'xs': 60,
                'ys': 60,
            },# }}}
        },
    }

def get_rgb(pic, box=""):# {{{
    if box == "":
        #box = (0, 0, pic.width, pic.height)
        box = (0, 0, pic.size[0], pic.size[1])
    # print "box: " + str(box)
    rgbimg = pic.crop(box).convert("RGB")
    rgb = numpy.array(rgbimg.getdata())
    # print(rgb)
    #return [__round(rgb[:,0]),
    #        __round(rgb[:,1]),
    #        __round(rgb[:,2])]
    rgb0 = __round(rgb[:, 0])
    rgb1 = __round(rgb[:, 1])
    rgb2 = __round(rgb[:, 2])
    return [rgb0, rgb1, rgb2]# }}}

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
    #    col["p"] = [120, 95,  115]    # poison
    else:
        col["1"] = [205, 110, 130]
        col["2"] = [100, 140, 190]
        col["3"] = [100, 160, 120]
        col["4"] = [200, 175, 110]
        col["5"] = [165, 90, 170]
        col["6"] = [200, 100, 150]
        col["7"] = [45,  45,  55]     # ojama
    #    col["8"] = [120, 95,  115]    # poison

# before_canMove
#
# rgb: [84, 65, 48]
# rgb: [110, 80, 55]
# rgb: [99, 64, 58]
# rgb: [110, 62, 63]
# rgb: [77, 61, 44]
# rgb: [94, 75, 73]
# rgb: [100, 64, 59]
# rgb: [111, 63, 64]
# rgb: [100, 64, 59]
# rgb: [84, 71, 54]
# rgb: [100, 65, 59]
# rgb: [125, 78, 65]
# rgb: [66, 62, 52]
# rgb: [104, 62, 68]
# rgb: [73, 45, 58]
# rgb: [91, 77, 59]
# rgb: [69, 61, 66]
# rgb: [109, 79, 55]
# rgb: [88, 50, 58]
# rgb: [97, 58, 64]
# rgb: [81, 50, 63]
# rgb: [109, 80, 55]
# rgb: [86, 66, 49]
# rgb: [91, 73, 72]
# rgb: [62, 56, 62]
# rgb: [104, 76, 52]
# rgb: [60, 58, 48]
# rgb: [105, 59, 61]
# rgb: [62, 56, 62]
# rgb: [96, 71, 47]
# llrrlrrrrlrrlrclclrrcllrdllrdl
#
# llrclbrcrgrrgddgblcddllbblgcbl
#    * * * *  ***** ***  ** ***

# after_canMove
#
# rgb: [168, 157, 95]
# rgb: [175, 160, 96]
# rgb: [193, 142, 127]
# rgb: [180, 91, 130]
# rgb: [157, 147, 86]
# rgb: [109, 138, 167]
# rgb: [195, 143, 129]
# rgb: [181, 91, 130]
# rgb: [194, 142, 128]
# rgb: [89, 136, 99]
# rgb: [196, 145, 130]
# rgb: [201, 147, 131]
# rgb: [92, 141, 105]
# rgb: [152, 91, 148]
# rgb: [138, 82, 140]
# rgb: [100, 147, 109]
# rgb: [102, 134, 165]
# rgb: [173, 159, 95]
# rgb: [175, 89, 130]
# rgb: [144, 85, 143]
# rgb: [150, 92, 151]
# rgb: [175, 161, 97]
# rgb: [168, 155, 93]
# rgb: [105, 135, 165]
# rgb: [92, 125, 157]
# rgb: [168, 156, 92]
# rgb: [85, 135, 101]
# rgb: [174, 87, 127]
# rgb: [93, 126, 157]
# rgb: [157, 146, 83]
# llrclbrcrgrrgddgblcddllbblgcbl

    max = 0
    result = ""
    for k, c in list(col.items()):
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
    # print(key1)
    # print(key2)
    edges = {
            'xa': 0,
            'ya': 0,
            'xb': 0,
            'yb': 0,
            'xs': 0,
            'ys': 0,
        }

    if key1 in pic_parm:
        if key2 in pic_parm[key1]:
            for k in list(edges.keys()):
                edges[k] = pic_parm[key1][key2][k]

    board = ""
    for i in range(cols):
        rows_rgb = get_rows_rgb(rows, edges, pic, i, flg)
        board += rows_rgb

    return board, key1, key2# }}}

def print_board(width, height, board):# {{{
    for h in range(height):
        print((board[h*width:h*width+width]))
    return 1# }}}

if __name__ == "__main__":
    import sys
    argvs = sys.argv

    if (len(argvs) != 4):
        print(("Usage: # python %s path width height" % argvs[0]))
        quit()

    #board = check_board(argvs[1], int(argvs[2]), int(argvs[3]), 0)

    path = ".\\" + argvs[1]
    board, key1, key2 = check_board(path, int(argvs[2]), int(argvs[3]), 0)
    print(board)
    print(key1)
    print(key2)
