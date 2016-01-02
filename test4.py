# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pazdracombo
import time
import multiprocessing

# 隣接リスト
adjacent_4x3 = [# {{{
        [1, 4],             #0
        [0, 2, 5],
        [1, 3, 6],
        [2, 7],
        [0, 5, 8],
        [1, 4, 6,  9],
        [2, 5, 7, 10],
        [3, 6, 11],
        [4, 9],
        [5, 8, 10],
        [6, 9, 11],
        [7, 10]
    ]# }}}

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

class Node:# {{{
    def __init__(self, start, board):
        self.score = 0
        self.combo = 0
        self.route = []
        self.route.append(start)
        self.board = board

    def set_route(self, lst):
        self.route = lst# }}}

def wrap_search_node_array(args):
    return args[0](*args[1:])

def search_node_array(width, height, max_turn, playnum, parms, start_board):# {{{
    node_array = []
    dummy_array = []

    for i in range(width * height):
        n = Node(i, start_board)
        node_array.append(n)

    for t in range(max_turn):
        for k in node_array:
            now_pos = k.route[-1]
            if len(k.route) != 1:
                prev_pos = k.route[-2]
            else:
                prev_pos = -1

            for j in get_adjacent(width, now_pos):
                if  j != prev_pos:
                    n = Node(k.route[0], k.board)
                    n.set_route(k.route[:])
                    n.board = swap(now_pos, j, k.board)
                    n.score, n.combo = calc_score(width, height, n.board, parms)
                    n.route.append(j)
                    if len(dummy_array) > playnum:
                        idx = 0
                        worst = 999999
                        for d,v in enumerate(dummy_array):
                            if worst > v.score:
                                worst = v.score
                                idx = d
                        del dummy_array[idx]
                    dummy_array.append(n)

            # i += 1
        node_array = []
        node_array = dummy_array[:]
        dummy_array = []

    return node_array# }}}

def Nbeam(width, height, start_board, max_turn, playnum, parms):

    node_array = search_node_array(width, height, max_turn, playnum, parms, start_board)

    idx = 0
    best = 0
    for k,v in enumerate(node_array):
        if best < v.score:
            best = v.score
            idx = k

    print "best score:" + str(node_array[idx].score)
    print "best combo:" + str(node_array[idx].combo)

    return node_array[idx]

def get_adjacent(width, now_pos):# {{{
    if width == 5:
        return adjacent_5x4[now_pos]
    elif width == 6:
        return adjacent_6x5[now_pos]
    else:
        return# }}}

def swap(a, b, board):# {{{
    i = int(a)
    j = int(b)
    if i > j:
        temp = i
        i = j
        j = temp
    li = list(board)
    temp = li[i]
    li[i] = li[j]
    li[j] = temp
    temp_board = "".join(li)
    return temp_board# }}}

def evalCombo(width, height, board):# {{{
    pdc = pazdracombo.PazdraComboChecker(width, height, board)
    pdc.check_erasable(width, height)
    pdc.calc_combo()
    return pdc.sum_combo()# }}}

def calc_score(width, height, board, parms):# {{{
    pdc = pazdracombo.PazdraComboChecker(width, height, board)
    pdc.check_erasable(width, height)
    pdc.calc_combo()
    return pdc.calc_score(parms)# }}}

if __name__ == '__main__':
    import multiprocessing as mp
    print "cpu count: " + str(mp.cpu_count())
    p = mp.Pool()
    func_args = []

    WIDTH = 6
    HEIGHT = 5

    MAX_TURN = 45
    PLAYNUM = 500

    DEFAULT_PARMS = {# {{{
            'name'  : "default",
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
            }# }}}

    parms = DEFAULT_PARMS

    start_board = "grllggglgrlrgrlrlggrlgggrlllrr"

    #node_array = search_node_array(WIDTH, HEIGHT, MAX_TURN, PLAYNUM, parms, start_board)
    #print len(node_array)

    func_args.append((search_node_array, WIDTH, HEIGHT, MAX_TURN, PLAYNUM, parms, start_board))
    results = p.map(wrap_search_node_array, func_args)
    print results

