# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

import numpy
from PIL import Image
import multiprocessing as mp
import itertools

class Board():

    PIC_PARM = {# {{{
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
        }# }}}

    DROP_RGB = {# {{{
            "r" : [205, 110, 130],
            "b" : [100, 140, 190],
            "g" : [100, 160, 120],
            "l" : [200, 175, 110],
            "d" : [165, 90,  170],
            "c" : [200, 100, 150],
            "o" : [45,  45,  55],    # ojama
            # "p" : [120, 95,  115],   # poison
            }# }}}

    def __init__(self, cols, rows, pic_path):# {{{
        self.cols = int(cols)
        self.rows = int(rows)
        self.pic_path = pic_path
        self.pic = Image.open(self.pic_path, 'r')
        self.pic_width = str(self.pic.size[0])
        self.pic_height = str(self.pic.size[1])
        self.edges = {# {{{
                'xa': 0,
                'ya': 0,
                'xb': 0,
                'yb': 0,
                'xs': 0,
                'ys': 0,
            }# }}}
        self.board = ""
        self.check_board()
        # }}}

    def get_rgb(self, pic, box=""):# {{{
        if box == "":
            box = (0, 0, pic.size[0], pic.size[1])
        rgbimg = pic.crop(box).convert("RGB")
        rgb = numpy.array(rgbimg.getdata())
        return [self.__round(rgb[:,0]),
                self.__round(rgb[:,1]),
                self.__round(rgb[:,2])]# }}}

    def color(self, array):# {{{
        max = 0
        result = ""
        for k, c in self.DROP_RGB.iteritems():
           tmp = numpy.corrcoef(numpy.array(array), numpy.array(c))[0][1]
           if max < tmp:
               result = k
               max = tmp
        return result# }}}

    def __round(self, array):# {{{
        return int(round(numpy.average(array)))# }}}

    def wrap_func(self, args):# {{{
        return args[0](*args[1:])# }}}

    def get_rows_rgb(self, col):# {{{
        rows_rgb = ""
        for row in range(self.rows):
            box = (self.edges['xa'] + self.edges['xs'] * col,
                   self.edges['ya'] + self.edges['ys'] * row,
                   self.edges['xb'] + self.edges['xs'] * col,
                   self.edges['yb'] + self.edges['ys'] * row)
            rgb = self.get_rgb(self.pic, box)
            rows_rgb += self.color(rgb)
        return rows_rgb# }}}

    def check_board(self):# {{{
        key1 = str(self.pic_width)
        key2 = str(self.cols)+"x"+str(self.rows)
        if self.PIC_PARM.has_key(key1):
            if self.PIC_PARM[key1].has_key(key2):
                for k in self.edges.keys():
                    self.edges[k] = self.PIC_PARM[key1][key2][k]

        for col in range(self.cols):
            self.board += self.get_rows_rgb(col)

        #return self.board, self.pic_width
    # }}}

    def print_board(game_parms, board):# {{{
        for h in range(game_parms.height):
            print board[ h * game_parms.width : h * game_parms.width + game_parms.width ]
        return 1# }}}

    # ドロップの行と列を入れ替える
    def convert_r_c(self, lst): # {{{{
        lst2 = []
        for row in range(self.rows):
            for col in range(self.cols):
                lst2.append(lst[self.rows * col + row])
        strs = "".join(list(itertools.chain.from_iterable(lst2)))
        return strs
        # }}}

if __name__ == "__main__":
    import sys
    argvs = sys.argv

    if (len(argvs) != 4):
        print "Usage: # python %s pic_path cols rows" % argvs[0]
        quit()

    pic_path = ".\\" + argvs[1]
    pad_board = Board(argvs[2], argvs[3], pic_path)
    print str(pad_board.board) + "," + str(pad_board.pic_width)
    # temp_board = pad_board.convert_r_c(pad_board.board)
    # print temp_board
