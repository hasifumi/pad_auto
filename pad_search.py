# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pazdracombo
import time

#MAX_TURN = 20
MAX_TURN = 10
#PLAYNUM = 5000
PLAYNUM = 100

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
        self.route = []
        self.route.append(start)
        self.board = board

    def set_route(self, lst):
        self.route = lst

    #def copy(self):
    #    #temp1 = { 'score': self.score, 'route': self.route[:], 'board': self.board }
    #    #print temp1.score
    #    #print temp1.route
    #    #print temp1.board
    #    # temp.score = self.score
    #    # temp.route = self.route[:]
    #    # temp.board = self.board
    #    #return temp
    #    temp = dict(score=self.score, route=self.route, board=self.board)
    #    print temp["score"]
    #    return self.score# }}}

def Nbeam(width, height, start_board):
    print "start_board:" + str(start_board)
    node_array = []
    dummy_array = []
    #dummy_size = 0

    for i in range(width * height):
        n = Node(i, start_board)
        node_array.append(n)

    for t in range(MAX_TURN):
        for k in node_array:
            now_pos = k.route[-1]
            if len(k.route) != 1:
                prev_pos = k.route[-2]
            else:
                prev_pos = -1
            if width == 4:
                for j in adjacent_4x3[now_pos]:
                    if  j != prev_pos:
                        n = Node(k.route[0], k.board)
                        n.set_route(k.route[:])
                        #n = k.copy()
                        n.board = swap(now_pos, j, k.board)
                        n.score = evalCombo(width, height, n.board)
                        n.route.append(j)
                        dummy_array.append(n)
            if width == 6:
                for j in adjacent_6x5[now_pos]:
                    if  j != prev_pos:
                        n = Node(k.route[0], k.board)
                        n.set_route(k.route[:])
                        #n = k.copy()
                        n.board = swap(now_pos, j, k.board)
                        #print n.board
                        n.score = evalCombo(width, height, n.board)
                        #print n.score
                        n.route.append(j)
                        #if i == PLAYNUM:
                        #    idx = 0
                        #    worst = 999999
                        #    for k,v in enumerate(node_array):
                        #        if worst > v.score:
                        #            worst = v.score
                        #            idx = k
                        #    if worst > n.score:
                        #        break
                        #    else:
                        #        del node_array[idx]
                        dummy_array.append(n)
                        #print "k:" + str(k) + ",len:" + str(len(dummy_array))
            i += 1
        node_array = dummy_array[:]
        dummy_array = []

    idx = 0
    best = 0
    for k,v in enumerate(node_array):
        if best < v.score:
            best = v.score
            idx = k

    print "len(node_array):" + str(len(node_array))
    print "best:" + str(best)
    print "idx:" + str(idx)
    print "route:" + str(node_array[idx].route)
    print "board:" + str(node_array[idx].board)

    return node_array[idx]

def swap(a, b, board):
    i = int(a)
    j = int(b)
    if i > j:
        temp = i
        i = j
        j = temp
    #print "swap i:" + str(i) + ", j:" + str(j) + ", board:" + str(board) + ", length:" + str(len(board))
    li = list(board)
    temp = li[i]
    li[i] = li[j]
    li[j] = temp
    temp_board = "".join(li)
    #print "swap return:" + str(temp_board) + ", length:" + str(len(temp_board))
    return temp_board

def evalCombo(width, height, board):
    #return 100
    pdc = pazdracombo.PazdraComboChecker(width, height, board)
    pdc.check_erasable()
    pdc.calc_combo()
    return pdc.sum_combo()

#Nbeam(4, 3, "rrbglggldgdc")

default_param = """
rddbgb
rrrbgb
rllbgb
ggggbb
clllll
""".replace('\n', '')

#start_time = time.time()
#
#n_best = Nbeam(6, 5, default_param)
#print n_best.score
#print n_best.route
#
#elapsed_time = time.time() - start_time
#print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
