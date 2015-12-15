# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#MAX_TURN = 20
MAX_TURN = 2
#PLAYNUM = 5000
PLAYNUM = 100

# 隣接リスト
adjacent_4x3 = [
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
    ]

adjacent_6x5 = [
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
]


class Node:
    def __init__(self, start, board):
        self.score = 0
        self.route = []
        self.route.append(start)
        self.board = board

    def copy(self):
        return self

def Nbeam(width, height, start_board):
    node_array = []

    for i in range(width * height):
        n = Node(i, start_board)
        node_array.append(n)

    for t in range(MAX_TURN):
        i = 0
        while len(node_array) < PLAYNUM:
            #print len(node_array[i].route)
            now_pos = node_array[i].route[len(node_array[i].route) - 1]
            if len(node_array[i].route) != 1:
                prev_pos = node_array[i].route[len(node_array[i].route) - 2]
            else:
                prev_pos = -1
            if width == 4:
                for j in adjacent_4x3[now_pos]:
                    if  j != prev_pos:
                        n = node_array[i].copy()
                        n.board = swap(now_pos, j, node_array[i].board)
                        n.score = evalCombo(n.board)
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
                        node_array.append(n)
                        print "i:" + str(i) + ",len:" + str(len(node_array))
            i += 1

    idx = 0
    best = 0
    for k,v in enumerate(node_array):
        if best < v.score:
            best = v.score
            idx = k
    print node_array[idx].route
    print node_array[idx].score
    print node_array[len(node_array)-1].route
    print node_array[len(node_array)-1].score

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

def evalCombo(board):
    return 100

Nbeam(4, 3, "rrbglggldgdc")
