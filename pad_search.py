# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

ROW = 5
COL = 6

MAX_TURN = 20
PLAYNUM = 5000

max_count = 0
start = []
start.append(11)
start.append(12)
print start

movei = [MAX_TURN][2]
goal = [2]

ans_start = [2]
ans = [MAX_TURN][2]
ans_goal = [2]
g_turn = 0

field = [ROW][COL]
chainflag = [ROW][COL]
t_erase = [ROW][COL]
dummy = [ROW][COL]
f_field = [ROW][COL]
fff = 0

class Node():# {{{
    def __init__(self):
        self.start[2]
        self.goal[2]
        self.movei[MAX_TURN][2]
        self.score
        self.nowR
        self.nowC# }}}

def Nbeam():
    """ Nbeam """
    node_array = []
    node_dum = []

    for i in range(PLAYNUM):# {{{
        n = Node()
        n.score = 0
        for t in range(MAX_TURN):
            n.movie[t][0] = -1
            n.movie[t][1] = -1
        node_array.append(n)# }}}

    size = ROW * COL

    cnt = 0
    for i in range(ROW):# {{{
        for j in range(COL):
            node_array[cnt].start[1] = j
            node_array[cnt].start[0] = i
            node_array[cnt].nowC = j
            node_array[cnt].nowR = i
            cnt += 1# }}}

    dx[4] = [ 0, -1, 1, 0]
    dy[4] = [-1,  0, 0, 1]

    for i in range(MAX_TURN):
        dumsize = 0
        for k in range(size):
            for j in range(len(dx)):
                temp = node_array[k]
                if (0 <= temp.nowC + dx[j]) and (temp.nowC + dx[j] < COL) and (0 <= temp.nowR + dy[j]) and (temp.nowR + dy[j] < ROW):
                    start[0] = temp.start[0]
                    start[1] = temp.start[1]
                    movei = temp.movei
                    temp.nowC += dx[j]
                    temp.nowR += dy[j]
                    goal[0] = temp.nowR
                    goal[1] = temp.nowC

                    if (i == MAX_TURN):
                        temp.goal[0] = temp.nowR
                        temp.goal[1] = temp.nowC
                    else:
                        temp.movei[i][0] = temp.nowR
                        temp.movei[i][1] = temp.nowC

                    operation()

                    temp.score = sum_e()

                    if (dumsize < PLAYNUM):
                        dum[dumsize] = temp
                        dumsize += 1
                    elif (dumsize == PLAYNUM):
                        rank = check2(PLAYNUM)
                        if (temp.score > dum[rank].score):
                            dum[rank] = temp

        for d in range(dumsize):
            node_array[d] = dum[d]

    size = dumsize

def operation():
    now_row = start[0]
    now_col = start[1]

    for i in rage(MAX_TURN):
        if movei[i][0] == -1 or movei[i][1] == -1:
            continue
        else:
            temp = field[now_row][now_col]
            field[now_row][now_col] = field[movei[i][0]][movei[i][1]]
            field[movei[i][0]][movei[i][1]] = temp
            now_row = movei[i][0]
            now_col = movei[i][1]

    temp = field[now_row][now_col]
    field[now_row][now_col] = field[goal[0]][goal[1]]
    field[goal[0]][goal[1]] = temp









