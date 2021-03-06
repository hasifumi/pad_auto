# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

# A tiny combo checker for Puzzle & Dragons
#   by takehikom (http://d.hatena.ne.jp/takehikom/)

import itertools
import copy
#import pad
#import padboard
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
        #self.combo = []
        self.combo = {}
        self.combo_count = 0
        self.combo_seq = {}
        self.combo_color = {}
        self.combo_color_count = {}  # cure以外の属性（色）カウンタ（例：3色）
        self.combo_cure_count = {}
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

    def make_renketsu(self, vector):# {{{
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
        return ary# }}}

    def check_erasable(self, width=6, height=5):# {{{
        ers = 0
        # 横方向の消去可能性チェック
        for j in range(height):
            for i in range(width - 2):
                if self.isRenketsu(i, j, "h") == True:
                    self.erase_l[j][i] = self.str_e(ers)
                    self.erase_l[j][i+1] = self.str_e(ers)
                    self.erase_l[j][i+2] = self.str_e(ers)
                    #self.combo.append([ers, i, j, "h", self.board_l[j][i], ers])
                    self.combo[ers] = {
                            'start_x_pos': i,
                            'start_y_pos': j,
                            'vector': "h",
                            'color': self.board_l[j][i],
                            'combo_seq': ers,
                            }
                    # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
                    ers += 1
        # 縦方向の消去可能性チェック
        for j in range(height - 2):
            for i in range(width):
                if self.isRenketsu(i, j, "v") == True:
                    self.erase_l[j][i] = self.str_e(ers)
                    self.erase_l[j+1][i] = self.str_e(ers)
                    self.erase_l[j+2][i] = self.str_e(ers)
                    #self.combo.append([ers, i, j, "v", self.board_l[j][i], ers])
                    self.combo[ers] = {
                            'start_x_pos': i,
                            'start_y_pos': j,
                            'vector': "v",
                            'color': self.board_l[j][i],
                            'combo_seq': ers,
                            }
                    # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
                    ers += 1# }}}

    def check_renkentsu_erasable(self, width=6, height=5):# {{{
        cmb_l = list(self.board)
        cnt = 0
        for k, v in self.combo.items():
            if v['vector'] == "h":
                for j in self.renketsu_h[self.xy2idx(v['start_x_pos'], v['start_y_pos'])]:
                    cmb_l[j] = self.str_e(v['combo_seq'])
            elif v['vector'] == "v":
                for j in self.renketsu_v[self.xy2idx(v['start_x_pos'], v['start_y_pos'])]:
                    cmb_l[j] = self.str_e(v['combo_seq'])
        # for i in self.combo:# {{{
        #     if i[3] == "h":
        #         for j in self.renketsu_6x5_h[self.xy2idx(i[1], i[2])]:
        #             cmb_l[j] = self.str_e(i[5])
        #     elif i[3] == "v":
        #         for j in self.renketsu_6x5_v[self.xy2idx(i[1], i[2])]:
        #             cmb_l[j] = self.str_e(i[5])# }}}
        self.erase2_l = cmb_l# }}}

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

    # グループ1の各ドロップの近接リストにグループ2の各ドロップが存在するかを調査する関数
    def isKinsetsu(self, x1, y1, v1, x2, y2, v2):  # x:x座標、y:y座標, v:方向# {{{
        idx1 = self.xy2idx(x1, y1)
        idx2 = self.xy2idx(x2, y2)
        if v1 == "h":
            for i in self.renketsu_h[idx1]:
                for j in self.adjacent[i]:
                    if v2 == "h":
                        for k in self.renketsu_h[idx2]:
                            if j == k:
                                return True
                    elif v2 == "v":
                        for k in self.renketsu_v[idx2]:
                            if j == k:
                                return True
        elif v1 == "v":
            for i in self.renketsu_v[idx1]:
                for j in self.adjacent[i]:
                    if v2 == "h":
                        for k in self.renketsu_h[idx2]:
                            if j == k:
                                return True
                    elif v2 == "v":
                        for k in self.renketsu_v[idx2]:
                            if j == k:
                                return True
        # if v1 == "h":# {{{
        #    if self.width == 5:
        #        for i in self.renketsu_5x4_h[idx1]:
        #            for j in self.adjacent_5x4[i]:
        #                if v2 == "h":
        #                    for k in self.renketsu_5x4_h[idx2]:
        #                        if j == k:
        #                            return True
        #                elif v2 == "v":
        #                    for k in self.renketsu_5x4_v[idx2]:
        #                        if j == k:
        #                            return True
        #    if self.width == 6:
        #        for i in self.renketsu_6x5_h[idx1]:
        #            for j in self.adjacent_6x5[i]:
        #                if v2 == "h":
        #                    for k in self.renketsu_6x5_h[idx2]:
        #                        if j == k:
        #                            return True
        #                elif v2 == "v":
        #                    for k in self.renketsu_6x5_v[idx2]:
        #                        if j == k:
        #                            return True
        # elif v1 == "v":
        #    if self.width == 5:
        #        for i in self.renketsu_5x4_v[idx1]:
        #            for j in self.adjacent_5x4[i]:
        #                if v2 == "h":
        #                    for k in self.renketsu_5x4_h[idx2]:
        #                        if j == k:
        #                            return True
        #                elif v2 == "v":
        #                    for k in self.renketsu_5x4_v[idx2]:
        #                        if j == k:
        #                            return True
        #    if self.width == 6:
        #        for i in self.renketsu_6x5_v[idx1]:
        #            for j in self.adjacent_6x5[i]:
        #                if v2 == "h":
        #                    for k in self.renketsu_6x5_h[idx2]:
        #                        if j == k:
        #                            return True
        #                elif v2 == "v":
        #                    for k in self.renketsu_6x5_v[idx2]:
        #                        if j == k:
        #                            return True# }}}
        return False# }}}

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

    def print_lst2str(self, mod="board"):# {{{
        if mod == "board":
            lst = copy.deepcopy(self.board_l)
        elif mod == "erase":
            lst = copy.deepcopy(self.erase_l)
        elif mod == "erase2":
            lst = copy.deepcopy(self.erase2_l)

        strs = "".join(list(itertools.chain.from_iterable(lst)))
        for h in range(self.height):
            print((strs[h*self.width:h*self.width+self.width]))
        #return# }}}

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
            print((strs[h*self.width:h*self.width+self.width]))
        return# }}}

    def calc_combo(self):# {{{
        cmb = -1
        cmb_keys = {}
        cmb_seq = {}
        cmb_color = {}
        cmb_color_count = 0  # cure以外の属性（色）カウンタ　（例：3色）
        cmb_cure_count = 0
        for k, v in self.combo.items():
            if k in cmb_keys:
                cmb_keys[k] += 1
            else:
                cmb_keys[k] = 1
            if cmb < v['combo_seq']:
                cmb += 1
                cmb_seq[cmb] = {
                        'first_find_seq': k,
                        'color': v['color'],
                        'vector': v['vector'],
                        'count': 1,
                        }
                if v['color'] in cmb_color:
                    cmb_color[v['color']] += 1
                else:
                    cmb_color[v['color']] = 1
                    if v['color'] == 'c':
                        cmb_cure_count += 1
                    else:
                        cmb_color_count += 1
            for k2, v2 in self.combo.items():
                if k2 in cmb_keys:
                    pass
                else:
                    if v['color'] == v2['color']:   # 同色か？
                        # vの各ドロップの近接リストにcmb2の各ドロップがいるか？
                        if self.isKinsetsu(v['start_x_pos'], v['start_y_pos'], v['vector'], v2['start_x_pos'], v2['start_y_pos'], v2['vector']):
                            v['combo_seq'] = cmb
                            v2['combo_seq'] = cmb
                            cmb_seq[cmb]['count'] += 1
        self.combo_count = cmb + 1
        self.combo_seq = cmb_seq
        self.combo_color = cmb_color
        self.combo_color_count = cmb_color_count
        self.combo_cure_count = cmb_cure_count
        return # }}}

    # def sum_combo(self):# {{{
    #     cmb = {}
    #     for k, v in self.combo.iteritems():
    #         if v['combo_seq'] in cmb:
    #             cmb[v['combo_seq']] += 1
    #         else:
    #             cmb[v['combo_seq']] = 1
    #     # for k in self.combo:
    #     #     if k[5] in cmb:
    #     #         cmb[k[5]] += 1
    #     #     else:
    #     #         cmb[k[5]] = 1
    #     return len(cmb)# }}}

    def calc_score(self, PARMS):# {{{
        score = 0

        # コンボ優先
        score += self.combo_count * 100

        # 属性優先（色優先）
        for k, v in self.combo_color.items():# {{{
            if   k == "r":
                if 'red' in PARMS:
                    score += PARMS['red'] * 100
            elif k == "b":
                if 'blue' in PARMS:
                    score += PARMS['blue'] * 100
            elif k == "g":
                if 'green' in PARMS:
                    score += PARMS['green'] * 100
            elif k == "l":
                if 'light' in PARMS:
                    score += PARMS['light'] * 100
            elif k == "d":
                if 'dark' in PARMS:
                    score += PARMS['dark'] * 100
            elif k == "c":
                if 'cure' in PARMS:
                    score += PARMS['cure'] * 100# }}}

        # 多色
        if self.combo_color_count >= 3 and '3colors' in PARMS:
            score += PARMS['3colors'] * 1000
        if self.combo_color_count >= 3 and self.combo_cure_count >= 1 and '3colors+cure' in PARMS:
            score += PARMS['3colors+cure'] * 1000
        if self.combo_color_count >= 4 and '4colors' in PARMS:
            score += PARMS['4colors'] * 1000
        if self.combo_color_count >= 4 and self.combo_cure_count >= 1 and '4colors+cure' in PARMS:
            score += PARMS['4colors+cure'] * 1000
        if self.combo_color_count >= 5 and '5colors' in PARMS:
            score += PARMS['5colors'] * 1000
        if self.combo_color_count >= 5 and self.combo_cure_count >= 1 and '5colors+cure' in PARMS:
            score += PARMS['5colors+cure'] * 1000# }}}

        # 列優先
        color = self.chk_1LineColor()# {{{
        for k, v in color.items():
            if   v == 'r' and '1line-red' in PARMS:
                score += PARMS['1line-red']  * 10000
            elif v == 'b' and '1line-blue' in PARMS:
                score += PARMS['1line-blue'] * 10000
            elif v == 'g' and '1line-green' in PARMS:
                score += PARMS['1line-green'] * 10000
            elif v == 'l' and '1line-light' in PARMS:
                score += PARMS['1line-light'] * 10000
            elif v == 'd' and '1line-dark' in PARMS:
                score += PARMS['1line-dark'] * 10000
            elif v == 'c' and '1line-cure' in PARMS:
                score += PARMS['1line-cure'] * 10000# }}}

        # 4つ消し、5つ消し
        drops4 = self.chk_drops4()# {{{
        drops5 = self.chk_drops5()

        for k, v in drops4.items():
            if   k == 'r' and '4drops-red' in PARMS:
                score += PARMS['4drops-red'] * 5000
                if k in drops5:
                    score += PARMS['4drops-red'] * 5000 * -1     # 罰
            elif k == 'b' and '4drops-blue' in PARMS:
                score += PARMS['4drops-blue'] * 5000
                if k in drops5:
                    score += PARMS['4drops-blue'] * 5000 * -1    # 罰
            elif k == 'g' and '4drops-green' in PARMS:
                score += PARMS['4drops-green'] * 5000
                if k in drops5:
                    score += PARMS['4drops-green'] * 5000 * -1    # 罰
            elif k == 'l' and '4drops-light' in PARMS:
                score += PARMS['4drops-light'] * 5000
                if k in drops5:
                    score += PARMS['4drops-light'] * 5000 * -1    # 罰
            elif k == 'd' and '4drops-dark' in PARMS:
                score += PARMS['4drops-dark'] * 5000
                if k in drops5:
                    score += PARMS['4drops-dark'] * 5000 * -1    # 罰
            elif k == 'c' and '4drops-cure' in PARMS:
                score += PARMS['4drops-cure'] * 5000
                if k in drops5:
                    score += PARMS['4drops-cure'] * 5000 * -1    # 罰
        return (score, self.combo_count)# }}}

        for k, v in drops5.items():# {{{
            if   k == 'r' and '5drops-red' in PARMS:
                score += PARMS['5drops-red'] * 5000
                if k in drops4:
                    score += PARMS['5drops-red'] * 5000 * -1     # 罰
            elif k == 'b' and '5drops-blue' in PARMS:
                score += PARMS['5drops-blue'] * 5000
                if k in drops4:
                    score += PARMS['5drops-blue'] * 5000 * -1    # 罰
            elif k == 'g' and '5drops-green' in PARMS:
                score += PARMS['5drops-green'] * 5000
                if k in drops4:
                    score += PARMS['5drops-green'] * 5000 * -1    # 罰
            elif k == 'l' and '5drops-light' in PARMS:
                score += PARMS['5drops-light'] * 5000
                if k in drops4:
                    score += PARMS['5drops-light'] * 5000 * -1    # 罰
            elif k == 'd' and '5drops-dark' in PARMS:
                score += PARMS['5drops-dark'] * 5000
                if k in drops4:
                    score += PARMS['5drops-dark'] * 5000 * -1    # 罰
            elif k == 'c' and '5drops-cure' in PARMS:
                score += PARMS['5drops-cure'] * 5000
                if k in drops4:
                    score += PARMS['5drops-cure'] * 5000 * -1    # 罰# }}}

        return (score, self.combo_count)# }}}

    def chk_1LineColor(self):# {{{
        color = {}
        for y in range(self.height):
            for x in range(self.width):
                if y in color:
                    if color[y] != self.board[self.xy2idx(x, y)]:
                        color[y] = ""
                        break
                else:
                    color[y] = self.board[self.xy2idx(x, y)]
        return  color# }}}

    def chk_drops4(self):# {{{
        drops4 = {}
        for k, v in self.combo_seq.items():
            if v['count'] == 2:
                if v['color'] in drops4:
                    drops4[v['color']] += 1
                else:
                    drops4[v['color']] = 1
        return drops4# }}}

    def chk_drops5(self):# {{{
        drops5 = {}
        for k, v in self.combo_seq.items():
            if v['count'] == 4:   # why "count:4" is drop5?
                if v['color'] in drops5:
                    drops5[v['color']] += 1
                else:
                    drops5[v['color']] = 1
        return drops5# }}}

    def chk_drops_color(self):# {{{
        drops_color = {}
        for d in self.board:
            if d in drops_color:
                drops_color[d] += 1
            else:
                drops_color[d] = 1
        return drops_color# }}}

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
