# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#MAX_TURN = 20
MAX_TURN = 2
PLAYNUM = 5000

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
        self.movei = [ 0 for i in range(MAX_TURN)]
        self.movei[0] = start
        self.board = board

def Nbeam(width, height, start_board):
    node_array = []

    for i in range(width * height):
        n = Node(i, i, start_board)
        #print n.movei
        node_array.append(n)

    for n in range(len(node_array)):
        prev_turn = n
        node = node_array[n]
        for t in range(MAX_TURN):
            if width == 4:
                for j in adjacent_4x3[prev_turn]:
                    #print "n: " + str(n) + ", adjacent_4x3[n]: " + str(adjacent_4x3[k]) + ", j:" + str(j)
                    next_board = swap(prev_turn, j, node.movei.board)
                    score = combo(next_board)



    for i in range(MAX_TURN):
        for k in range(width * height):
            if width == 4:
                for j in adjacent_4x3[k]:
                    #print "k: " + str(k) + ", adjacent_4x3[k]: " + str(adjacent_4x3[k]) + ", j:" + str(j)
                    temp_board = swap(k, j,


def swap(a, b, board):
    temp_board = board
    temp = temp_board[a]
    temp_board[a] = temp_board[b]
    temp_board[b] = temp
    return temp_board

Nbeam(4, 3, "rrrr")
