# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

# A tiny combo checker for Puzzle & Dragons
#   by takehikom (http://d.hatena.ne.jp/takehikom/)

import itertools
import copy
#import pad
import padboard
import subprocess
import time

PARMS = {# {{{
        'red'  : 1.0,
        'blue' : 1.0,
        'green': 1.0,
        'light': 1.0,
        'dark' : 1.0,
        'cure' : 1.0,
        '4colors'  : 1.0,
        '5colors'  : 0.0,
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
        }# }}}

class PazdraComboChecker():

# {{{
    default_param = """
rddbgb
rrrbgb
rllbgb
ggggbb
clllll
""".replace('\n', '')

    pdc_combo_ascii_table = list("abcdefghij")

# }}}

    adjacent_5x4 = [# {{{
            [1, 5],             # 0
            [0, 2, 6],
            [1, 3, 7],
            [2, 4, 8],
            [3, 9],
            [0, 6, 10],
            [1, 5, 7, 11],
            [2, 6, 8, 12],
            [3, 7, 9, 13],
            [4, 8, 14],
            [5, 11, 15],
            [6, 10, 12, 16],
            [7, 11, 13, 17],
            [8, 12, 14, 18],
            [9, 13, 19],
            [10, 16],
            [11, 15, 17],
            [12, 16, 18],
            [13, 17, 19],
            [14, 18]
    ]# }}}

    renketsu_5x4_h = [# {{{
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [],
            [],
            [5, 6, 7],
            [6, 7, 8],
            [7, 8, 9],
            [],
            [],
            [10, 11, 12],
            [11, 12, 13],
            [12, 13, 14],
            [],
            [],
            [15, 16, 17],
            [16, 17, 18],
            [17, 18, 19],
            [],
            [],
    ]# }}}

    renketsu_5x4_v = [# {{{
            [0, 5, 10],
            [1, 6, 11],
            [2, 7, 12],
            [3, 8, 13],
            [4, 9, 14],
            [5, 10, 15],
            [6, 11, 16],
            [7, 12, 17],
            [8, 13, 18],
            [9, 14, 19],
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
            [2, 3, 4],
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

    def __init__(self, width, height, param=None):# {{{
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
        self.erase2_l = copy.deepcopy(self.board_l)
        self.fall_l = copy.deepcopy(self.board_l)
        self.combo = []
        self.adjacent = self.make_adjacent()
        self.renketsu_h = self.make_renketsu("h")
        self.renketsu_v = self.make_renketsu("v")
        # combo : 1)find_seq, 2)start_x_pos, 3)start_y_pos, 4)vector(h/v), 5)color, 6)combo_seq# }}}

    # 文字列を2二元配列に格納
    def str2lst(self, param, width, height):# {{{
        ret = [[0 for col in range(width)] for row in range(height)]
        if len(param) == width * height:
            i = 0
            for h in range(height):
                for w in range(width):
                    ret[h][w] = param[i]
                    i += 1
        #print ret
        return ret# }}}

    # ユーティリティ関数
    def xy2idx(self, x, y):# {{{
        return y*self.width+x# }}}

    def idx2xy(self, idx):# {{{
        return[int(idx/self.width), int(idx%self.width)]# }}}

    def make_adjacent(self):# {{{
        ary = []
        for h in range(self.height):
            for w in range(self.width):
                ary_b = []
                if 0 <= w - 1:
                    ary_b.append(self.xy2idx(w - 1, h))
                if w + 1 < self.width:
                    ary_b.append(self.xy2idx(w + 1, h))
                if 0 <= h - 1:
                    ary_b.append(self.xy2idx(w, h - 1))
                if h + 1 < self.height:
                    ary_b.append(self.xy2idx(w, h + 1))
                ary.append(ary_b)
        return ary# }}}

    def make_renketsu(self, vector):
        ary = []
        for h in range(self.height):
            for w in range(self.width):
                if vector == "h":  # horizon
                    if   w+2 < self.width:
                        ary.append([self.xy2idx(w, h), self.xy2idx(w+1, h), self.xy2idx(w+2, h)])
                    else:
                        ary.append([])
                elif vector == "v":  # vertical
                    if   h+2 < self.height:
                        ary.append([self.xy2idx(w, h), self.xy2idx(w, h+1), self.xy2idx(w, h+2)])
                    else:
                        ary.append([])
        return ary

    def check_erasable(self, width=6, height=5):# {{{
        ers = 0
        # 横方向の消去可能性チェック
        for j in range(height):
            for i in range(width - 2):
                if self.isRenketsu(i, j, "h") == True:
                    self.erase_l[j][i] = self.str_e(ers)
                    self.erase_l[j][i+1] = self.str_e(ers)
                    self.erase_l[j][i+2] = self.str_e(ers)
                    self.combo.append([ers, i, j, "h", self.board_l[j][i], ers])
                    ers += 1
        # 縦方向の消去可能性チェック
        for j in range(height - 2):
            for i in range(width):
                if self.isRenketsu(i, j, "v") == True:
                    self.erase_l[j][i] = self.str_e(ers)
                    self.erase_l[j+1][i] = self.str_e(ers)
                    self.erase_l[j+2][i] = self.str_e(ers)
                    self.combo.append([ers, i, j, "v", self.board_l[j][i], ers])
                    ers += 1# }}}

    def check_renkentsu_erasable(self, width=6, height=5):# {{{
        cmb_l = list(self.board)
        cnt = 0
        for i in self.combo:
            if i[3] == "h":
                for j in self.renketsu_6x5_h[self.xy2idx(i[1], i[2])]:
                    cmb_l[j] = self.str_e(i[5])
            elif i[3] == "v":
                for j in self.renketsu_6x5_v[self.xy2idx(i[1], i[2])]:
                    cmb_l[j] = self.str_e(i[5])
        self.erase2_l = cmb_l# }}}

    def str_e(self,e):# {{{
        if 0 <= e <= 9:
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

    def isRenketsu(self, x, y, vector="h"):# {{{
        #print "isRenketsu x:" + str(x) + ", y:" + str(y) + ", vector:" + str(vector)
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
            return False# }}}

    def print_lst2str(self, mod="board"):# {{{
        if mod == "board":
            lst = copy.deepcopy(self.board_l)
        elif mod == "erase":
            lst = copy.deepcopy(self.erase_l)
        elif mod == "erase2":
            lst = copy.deepcopy(self.erase2_l)

        strs = "".join(list(itertools.chain.from_iterable(lst)))
        for h in range(self.height):
            print strs[h*self.width:h*self.width+self.width]
        #return# }}}

    def calc_combo(self):# {{{
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
        return # }}}

    def sum_combo(self):# {{{
        cmb = {}
        for k in self.combo:
            if k[5] in cmb:
                cmb[k[5]] += 1
            else:
                cmb[k[5]] = 1
        return len(cmb)# }}}

    def calc_score(self, PARMS):# {{{
    #def calc_score(self, red=1.0, blue=1.0, green=1.0, light=1.0, dark=1.0, cure=1.0):
    # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
        cmb = {}
        color = {# {{{
                'r' : 0,
                'b' : 0,
                'g' : 0,
                'l' : 0,
                'd' : 0,
                'c' : 0,
                'o' : 0,
                'p' : 0,
                }# }}}
        colors = 0
        score = 0
        combo = 0

        for k in self.combo:
            if (k[5]) in cmb:
                cmb[(k[5])] = k[0]
            else:
                cmb[(k[5])] = k[0]
        combo = len(cmb)
        score += combo * 100

        # 属性優先
        for c in cmb.values():# {{{
            if self.combo[c][4] == 'r':
                color['r'] = 1
                if PARMS.has_key('red'):
                    score += PARMS['red'] * 100
            elif self.combo[c][4] == 'b':
                color['b'] = 1
                if PARMS.has_key('blue'):
                    score += PARMS['blue'] * 100
            elif self.combo[c][4] == 'g':
                color['g'] = 1
                if PARMS.has_key('green'):
                    score += PARMS['green'] * 100
            elif self.combo[c][4] == 'l':
                color['l'] = 1
                if PARMS.has_key('light'):
                    score += PARMS['light'] * 100
            elif self.combo[c][4] == 'd':
                color['d'] = 1
                if PARMS.has_key('dark'):
                    score += PARMS['dark'] * 100
            elif self.combo[c][4] == 'c':
                color['c'] = 1
                if PARMS.has_key('cure'):
                    score += PARMS['cure'] * 100# }}}

        # 多色
        for k in cmb.keys():# {{{
            if self.combo[cmb[k]][4] != 'c':
                if color[self.combo[cmb[k]][4]] != 0:
                    colors += 1
        if colors >= 3 and PARMS.has_key('3colors'):
            score += PARMS['3colors'] * 1000
        if colors >= 3 and color['c'] == 1 and PARMS.has_key('3colors+cure'):
            score += PARMS['3colors+cure'] * 1000
        if colors >= 4 and PARMS.has_key('4colors'):
            score += PARMS['4colors'] * 1000
        if colors >= 4 and color['c'] == 1 and PARMS.has_key('4colors+cure'):
            score += PARMS['4colors+cure'] * 1000
        if colors >= 5 and PARMS.has_key('5colors'):
            score += PARMS['5colors'] * 1000
        if colors >= 5 and color['c'] == 1 and PARMS.has_key('5colors+cure'):
            score += PARMS['5colors+cure'] * 1000# }}}

        # 列優先
        color = self.chk1LineColor()# {{{
        for k in color.keys():
            #print "k: " + str(k) + ", color[k]: " + str(color[k])
            if   color[k] == 'r' and PARMS.has_key('1line-red'):
                score += PARMS['1line-red']  * 10000
            elif color[k] == 'b' and PARMS.has_key('1line-blue'):
                score += PARMS['1line-blue'] * 10000
            elif color[k] == 'g' and PARMS.has_key('1line-green'):
                score += PARMS['1line-green'] * 10000
            elif color[k] == 'l' and PARMS.has_key('1line-light'):
                score += PARMS['1line-light'] * 10000
            elif color[k] == 'd' and PARMS.has_key('1line-dark'):
                score += PARMS['1line-dark'] * 10000
            elif color[k] == 'c' and PARMS.has_key('1line-cure'):
                score += PARMS['1line-cure'] * 10000# }}}

        # 4つ消し
        drops4 = self.chkdrops4()# {{{
        # drops4 emample = {0: [0, 0, 1, 'h', 'r', 1], 1: [4, 0, 1, 'h', 'b', 1]}
        for k in drops4.keys():
            if   drops4[k][4] == 'r' and PARMS.has_key('4drops-red'):
                #score += PARMS['4drops-red'] * 5000
                if   drops4[k][3] == "h" and drops4[k][2] > 1:
                    score += PARMS['4drops-red'] * 5000 * -1     # 罰
                elif drops4[k][3] == "v" and drops4[k][1] > 1:
                    score += PARMS['4drops-red'] * 5000 * -1     # 罰
                else:
                    score += PARMS['4drops-red'] * 5000
            elif drops4[k][4] == 'b' and PARMS.has_key('4drops-blue'):
                #score += PARMS['4drops-blue'] * 5000
                if   drops4[k][3] == "h" and drops4[k][2] > 1:
                    score += PARMS['4drops-blue'] * 5000 * -1     # 罰
                elif drops4[k][3] == "v" and drops4[k][1] > 1:
                    score += PARMS['4drops-blue'] * 5000 * -1     # 罰
                else:
                    score += PARMS['4drops-blue'] * 5000
            elif drops4[k][4] == 'g' and PARMS.has_key('4drops-green'):
                #score += PARMS['4drops-green'] * 5000
                if   drops4[k][3] == "h" and drops4[k][2] > 1:
                    score += PARMS['4drops-green'] * 5000 * -1     # 罰
                elif drops4[k][3] == "v" and drops4[k][1] > 1:
                    score += PARMS['4drops-green'] * 5000 * -1     # 罰
                else:
                    score += PARMS['4drops-green'] * 5000
            elif drops4[k][4] == 'l' and PARMS.has_key('4drops-light'):
                #score += PARMS['4drops-light'] * 5000
                if   drops4[k][3] == "h" and drops4[k][2] > 1:
                    score += PARMS['4drops-light'] * 5000 * -1     # 罰
                elif drops4[k][3] == "v" and drops4[k][1] > 1:
                    score += PARMS['4drops-light'] * 5000 * -1     # 罰
                else:
                    score += PARMS['4drops-light'] * 5000
            elif drops4[k][4] == 'd' and PARMS.has_key('4drops-dark'):
                #score += PARMS['4drops-dark'] * 5000
                if   drops4[k][3] == "h" and drops4[k][2] > 1:
                    score += PARMS['4drops-dark'] * 5000 * -1     # 罰
                elif drops4[k][3] == "v" and drops4[k][1] > 1:
                    score += PARMS['4drops-dark'] * 5000 * -1     # 罰
                else:
                    score += PARMS['4drops-dark'] * 5000# }}}

        return (score, combo)# }}}

    def chk1LineColor(self):# {{{
        color = {}
        for y in range(self.height):
            for x in range(self.width):
                if color.has_key(y):
                    if color[y] != self.board[self.xy2idx(x, y)]:
                        color[y] = ""
                        break
                else:
                    color[y] = self.board[self.xy2idx(x, y)]
        return  color# }}}

    def chkdrops4(self):# {{{
        # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
        drops4 = {}
        for k in self.combo:
            if drops4.has_key(k[5]):
                if k[3] == drops4[k[5]][3]:
                    drops4[k[5]][5] += 1
                    if k[3] == "h":
                        drops4[k[5]][2] += (k[1] - drops4[k[5]][1])   # start_y_posにx座標の差を加算
                    elif k[3] == "v":
                        drops4[k[5]][1] += (k[2] - drops4[k[5]][2])   # start_x_posにy座標の差を加算
            else:
                temp_k = [k[0], k[1], k[2], k[3], k[4], k[5]]
                temp_k[5] = 0
                if temp_k[3] == "h":
                    temp_k[2] = 0
                elif temp_k[3] == "v":
                    temp_k[1] = 0
                drops4[k[5]] = temp_k
        return drops4# }}}

    # グループ1の各ドロップの近接リストにグループ2の各ドロップが存在するかを調査する関数
    def isKinsetsu(self, x1, y1, v1, x2, y2, v2):  # x:x座標、y:y座標, v:方向# {{{
        idx1 = self.xy2idx(x1, y1)
        idx2 = self.xy2idx(x2, y2)
        if v1 == "h":
            if self.width == 5:
                for i in self.renketsu_5x4_h[idx1]:
                    for j in self.adjacent_5x4[i]:
                        if v2 == "h":
                            for k in self.renketsu_5x4_h[idx2]:
                                if j == k:
                                    return True
                        elif v2 == "v":
                            for k in self.renketsu_5x4_v[idx2]:
                                if j == k:
                                    return True
            if self.width == 6:
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
            if self.width == 5:
                for i in self.renketsu_5x4_v[idx1]:
                    for j in self.adjacent_5x4[i]:
                        if v2 == "h":
                            for k in self.renketsu_5x4_h[idx2]:
                                if j == k:
                                    return True
                        elif v2 == "v":
                            for k in self.renketsu_5x4_v[idx2]:
                                if j == k:
                                    return True
            if self.width == 6:
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
        return False# }}}

    def print_combo(self):# {{{
        # cmb_l = list(self.board)
        # for i in self.combo:
        #     if i[3] == "h":
        #         for j in self.renketsu_6x5_h[self.xy2idx(i[1], i[2])]:
        #             cmb_l[j] = self.str_e(i[5])
        #     elif i[3] == "v":
        #         for j in self.renketsu_6x5_v[self.xy2idx(i[1], i[2])]:
        #             cmb_l[j] = self.str_e(i[5])
        # strs = "".join(cmb_l)
        strs = "".join(self.erase2_l)
        for h in range(self.height):
            print strs[h*self.width:h*self.width+self.width]
        return# }}}

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
    strs = "".join(list(itertools.chain.from_iterable(lst2)))
    return strs# }}}

def convert_h_w_6x5(lst):# {{{
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
    strs = "".join(list(itertools.chain.from_iterable(lst2)))
    return strs# }}}

def convert_h_w_5x4(lst):# {{{
    lst2 = []
    lst2.append(lst[0])
    lst2.append(lst[4])
    lst2.append(lst[8])
    lst2.append(lst[12])
    lst2.append(lst[16])
    lst2.append(lst[1])
    lst2.append(lst[5])
    lst2.append(lst[9])
    lst2.append(lst[13])
    lst2.append(lst[17])
    lst2.append(lst[2])
    lst2.append(lst[6])
    lst2.append(lst[10])
    lst2.append(lst[14])
    lst2.append(lst[18])
    lst2.append(lst[3])
    lst2.append(lst[7])
    lst2.append(lst[11])
    lst2.append(lst[15])
    lst2.append(lst[19])
    strs = "".join(list(itertools.chain.from_iterable(lst2)))
    return strs# }}}

def convert_h_w_7x6(lst):# {{{
    lst2 = []
    lst2.append(lst[0])
    lst2.append(lst[6])
    lst2.append(lst[12])
    lst2.append(lst[18])
    lst2.append(lst[24])
    lst2.append(lst[30])
    lst2.append(lst[36])
    lst2.append(lst[1])
    lst2.append(lst[7])
    lst2.append(lst[13])
    lst2.append(lst[19])
    lst2.append(lst[25])
    lst2.append(lst[31])
    lst2.append(lst[37])
    lst2.append(lst[2])
    lst2.append(lst[8])
    lst2.append(lst[14])
    lst2.append(lst[20])
    lst2.append(lst[26])
    lst2.append(lst[32])
    lst2.append(lst[38])
    lst2.append(lst[3])
    lst2.append(lst[9])
    lst2.append(lst[15])
    lst2.append(lst[21])
    lst2.append(lst[27])
    lst2.append(lst[33])
    lst2.append(lst[39])
    lst2.append(lst[4])
    lst2.append(lst[10])
    lst2.append(lst[16])
    lst2.append(lst[22])
    lst2.append(lst[28])
    lst2.append(lst[34])
    lst2.append(lst[40])
    lst2.append(lst[5])
    lst2.append(lst[11])
    lst2.append(lst[17])
    lst2.append(lst[23])
    lst2.append(lst[29])
    lst2.append(lst[35])
    lst2.append(lst[41])
    strs = "".join(list(itertools.chain.from_iterable(lst2)))
    return strs# }}}
