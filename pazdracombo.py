# vim: foldmethod=marker  :
# -*- coding: utf-8 -*-

# A tiny combo checker for Puzzle & Dragons
#   by takehikom (http://d.hatena.ne.jp/takehikom/)

import itertools
import copy
import pad
import padboard
import subprocess
import time

class PazdraComboChecker():

    pdc_sym_table = {# {{{
            "1": "fire",
            "2": "water",
            "3": "wood",
            "4": "light",
            "5": "dark",
            "6": "cure",
            "r": "fire",
            "b": "water",
            "g": "wood",
            "l": "light",
            "d": "dark",
            "c": "cure",
    }# }}}

    pdc_output_ascii_table = {# {{{
            "fire"  : "1",
            "water" : "2",
            "wood"  : "3",
            "light" : "4",
            "dark"  : "5",
            "cure"  : "6",
    }# }}}

    default_param = """
rddbgb
rrrbgb
rllbgb
ggggbb
clllll
""".replace('\n', '')

    pdc_combo_ascii_table = list("abcdefghij")

    pdc_output_table = pdc_output_ascii_table
    pdc_combo_table = pdc_combo_ascii_table

    adjacent_6x5 = [# {{{
            [1, 6],             # 0
            [0, 2, 7],
            [1, 3, 8],
            [2, 4, 9],
            [3, 5, 10],
            [4, 11],
            [0, 7, 12],
            [1, 6, 8, 13],
            [2, 7, 9, 14],
            [3, 8, 10, 15],
            [4, 9, 11, 16],
            [5, 10, 17],
            [6, 13, 18],
            [7, 12, 14, 19],
            [8, 13, 15, 20],
            [9, 14, 16, 21],
            [10, 15, 17, 22],
            [11, 16, 23],
            [12, 19, 24],
            [13, 18, 20, 25],
            [14, 19, 21, 26],
            [15, 20, 22, 27],
            [16, 21, 23, 28],
            [17, 22, 29],
            [18, 25],
            [19, 24, 26],
            [20, 25, 27],
            [21, 26, 28],
            [22, 27, 29],
            [23, 28]
    ]# }}}

    renketsu_6x5_h = [# {{{
            [0, 1, 2],
            [1, 2, 3],
            [2,3, 4],
            [3, 4, 5],
            [],
            [],
            [6, 7, 8],
            [7, 8, 9],
            [8, 9, 10],
            [9, 10, 11],
            [],
            [],
            [12, 13, 14],
            [13, 14, 15],
            [14, 15, 16],
            [15, 16, 17],
            [],
            [],
            [18, 19, 20],
            [19, 20, 21],
            [20, 21, 22],
            [21, 22, 23],
            [],
            [],
            [24, 25, 26],
            [25, 26, 27],
            [26, 27, 28],
            [27, 28, 29],
            [],
            [],
    ]# }}}

    renketsu_6x5_v = [# {{{
            [0, 6, 12],
            [1, 7, 13],
            [2, 8, 14],
            [3, 9, 15],
            [4, 10, 16],
            [5, 11, 17],
            [6, 12, 18],
            [7, 13, 19],
            [8, 14, 20],
            [9, 15, 21],
            [10, 16, 22],
            [11, 17, 23],
            [12, 18, 24],
            [13, 19, 25],
            [14, 20, 26],
            [15, 21, 27],
            [16, 22, 28],
            [17, 23, 29],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
    ]# }}}


    def __init__(self, width, height, param=None):
        if param is None:
            param = self.default_param
            self.width = 6
            self.height = 5
        else:
            self.width = width
            self.height = height
        self.board = param
        self.board_l = self.str2lst(param, width, height)
        self.erase_l = copy.deepcopy(self.board_l)
        self.combo = []
        # combo : 1)find_seq, 2)start_x_pos, 3)start_y_pos, 4)vector(h/v), 5)color, 6)combo_seq

    # 文字列を2二元配列に格納
    def str2lst(self, param, width, height):
        ret = [[0 for col in range(width)] for row in range(height)]
        if len(param) == width * height:
            i = 0
            for h in range(height):
                for w in range(width):
                    ret[h][w] = param[i]
                    i += 1
        #print ret
        return ret

    # ユーティリティ関数
    def xy2idx(self, x, y):
        return y*self.width+x

    def idx2xy(self, idx):
        return[int(idx/self.width), int(idx%self.width)]

    def check_erasable(self, width=6, height=5):
        e = 0
        # 横方向の消去可能性チェック
        for j in range(height):
            for i in range(width - 2):
                #print "i: " + str(i) + ", j: " + str(j)
                if self.isRenketsu(i, j, "h") == True:
                    e += 1
                    self.erase_l[j][i] = self.str_e(e)
                    self.erase_l[j][i+1] = self.str_e(e)
                    self.erase_l[j][i+2] = self.str_e(e)
                    self.combo.append([e, i, j, "h", self.board_l[j][i], e])
        # 縦方向の消去可能性チェック
        for j in range(height - 2):
            for i in range(width):
                #print "i: " + str(i) + ", j: " + str(j)
                if self.isRenketsu(i, j, "v") == True:
                    e += 1
                    self.erase_l[j][i] = self.str_e(e)
                    self.erase_l[j+1][i] = self.str_e(e)
                    self.erase_l[j+2][i] = self.str_e(e)
                    self.combo.append([e, i, j, "v", self.board_l[j][i], e])

    def str_e(self,e):# {{{
        if 0 < e <= 9:
            return str(e)
        elif e == 10:
            return "A"
        elif e == 11:
            return "B"
        elif e == 12:
            return "C"
        elif e == 13:
            return "D"
        elif e == 14:
            return "E"
        elif e == 15:
            return "F"
        elif e == 16:
            return "G"
        elif e == 17:
            return "H"
        elif e == 18:
            return "I"
        elif e == 19:
            return "J"
        elif e == 20:
            return "K"
        elif e > 20:
            return "Z"# }}}

    def isRenketsu(self, x, y, vector="h"):
        if vector == "h":  # 横方向
            if self.board_l[y][x] == self.board_l[y][x+1] == self.board_l[y][x+2]:
                return True
            else:
                return False
        elif vector == "v":  # 縦方向
            if self.board_l[y][x] == self.board_l[y+1][x] == self.board_l[y+2][x]:
                return True
            else:
                return False
        else:
            return False

    def print_lst2str(self, mod="board"):
        if mod == "board":
            lst = copy.deepcopy(self.board_l)
        elif mod == "erase":
            lst = copy.deepcopy(self.erase_l)

        strs = "".join(list(itertools.chain.from_iterable(lst)))
        for h in range(self.height):
            print strs[h*self.width:h*self.width+self.width]
        #return

    def calc_combo(self):
        cmb = 0
        for i, v in enumerate(self.combo):
            if cmb < v[5]:
                cmb += 1
            for i2, v2 in enumerate(self.combo[i+1:]):
                if v[4] == v2[4]:   # 同色か？
                    # vの各ドロップの近接リストにcmb2の各ドロップがいるか？
                    if self.isKinsetsu(v[1], v[2], v[3], v2[1], v2[2], v2[3]):
                        self.combo[i][5] = cmb
                        self.combo[i+i2+1][5] = cmb
                        #print "cmb:" + str(cmb) + ", i:" + str(i) + ", i2:" + str(i2) + ", i+i2+1:" + str(i+i2+1) + ", self.combo[i+i2+1][5]: " + str(self.combo[i+i2+1][5])
        return

    def sum_combo(self):
        cmb = {}
        for k in self.combo:
            if k[5] in cmb:
                cmb[k[5]] += 1
            else:
                cmb[k[5]] = 1
        return len(cmb)

    # グループ1の各ドロップの近接リストにグループ2の各ドロップが存在するかを調査する関数
    def isKinsetsu(self, x1, y1, v1, x2, y2, v2):  # x:x座標、y:y座標, v:方向
        idx1 = self.xy2idx(x1, y1)
        idx2 = self.xy2idx(x2, y2)
        if v1 == "h":
            for i in self.renketsu_6x5_h[idx1]:
                for j in self.adjacent_6x5[i]:
                    if v2 == "h":
                        for k in self.renketsu_6x5_h[idx2]:
                            if j == k:
                                return True
                    elif v2 == "v":
                        for k in self.renketsu_6x5_v[idx2]:
                            if j == k:
                                return True
        elif v1 == "v":
            for i in self.renketsu_6x5_v[idx1]:
                for j in self.adjacent_6x5[i]:
                    if v2 == "h":
                        for k in self.renketsu_6x5_h[idx2]:
                            if j == k:
                                return True
                    elif v2 == "v":
                        for k in self.renketsu_6x5_v[idx2]:
                            if j == k:
                                return True
        return False

    def print_combo(self):
        cmb_l = list(self.board)
        for i in self.combo:
            if i[3] == "h":
                for j in self.renketsu_6x5_h[self.xy2idx(i[1], i[2])]:
                    cmb_l[j] = self.str_e(i[5])
            elif i[3] == "v":
                for j in self.renketsu_6x5_v[self.xy2idx(i[1], i[2])]:
                    cmb_l[j] = self.str_e(i[5])
        strs = "".join(cmb_l)
        for h in range(self.height):
            print strs[h*self.width:h*self.width+self.width]
        return


    # 妥当なブロックか判定# {{{
    def pdc_valid(self, sym):
        if sym == "fire" or "water" or "wood" or "light" or "dark" or "cure":
            return True
        else:
            return False# }}}

def convert_h_w(lst):# {{{
    lst2 = []
    lst2.append(lst[0])
    lst2.append(lst[5])
    lst2.append(lst[10])
    lst2.append(lst[15])
    lst2.append(lst[20])
    lst2.append(lst[25])
    lst2.append(lst[1])
    lst2.append(lst[6])
    lst2.append(lst[11])
    lst2.append(lst[16])
    lst2.append(lst[21])
    lst2.append(lst[26])
    lst2.append(lst[2])
    lst2.append(lst[7])
    lst2.append(lst[12])
    lst2.append(lst[17])
    lst2.append(lst[22])
    lst2.append(lst[27])
    lst2.append(lst[3])
    lst2.append(lst[8])
    lst2.append(lst[13])
    lst2.append(lst[18])
    lst2.append(lst[23])
    lst2.append(lst[28])
    lst2.append(lst[4])
    lst2.append(lst[9])
    lst2.append(lst[14])
    lst2.append(lst[19])
    lst2.append(lst[24])
    lst2.append(lst[29])
    #print lst2
    strs = "".join(list(itertools.chain.from_iterable(lst2)))
    return strs# }}}
