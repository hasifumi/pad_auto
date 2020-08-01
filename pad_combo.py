# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import numpy as np
import random
import copy
# from numba import jit

COL = 6
ROW = 5
MAX_TURN = 50
BEAM_WIDTH = 1000
DROPS = 6
DROP = [" rbgldcop*    "]
# DROP = {{{{
#     0: " ", # null, space
#     1: "r", # red
#     2: "b", # blue
#     3: "g", # green
#     4: "l", # light
#     5: "d", # dark
#     6: "c", # cure
#     7: "o", # ojama
#     8: "p", # poison
#     9: "*", # else,,,
#     }}}}

field = np.zeros((ROW, COL), dtype=int)
# f_field = np.zeros((ROW, COL), dtype=int)
chainflag = np.zeros((ROW, COL), dtype=int)
dummy = np.zeros((ROW, COL), dtype=int)
t_erace = np.zeros((ROW, COL), dtype=int)
max_count = 0
route = np.full((MAX_TURN, 2), -1, dtype=int)  # example [[r1 c1], [r2 c2], [r3 c3],,,,]

def set_field(field, field1=""):# {{{
    fld = field.copy()
    if len(field1) == 0:
        for r in np.arange(ROW):
            for c in np.arange(COL):
                if field[r, c] == 0:
                    fld[r, c] = random.randint(1, DROPS)
    else:
        for r in np.arange(ROW):
            for c in np.arange(COL):
                fld[r, c] = field1[c+r*COL]
    return fld# }}}

def show_field(field1):# {{{
    if len(field1):
        for r in np.arange(ROW):
            drps = ""
            for c in np.arange(COL):
                drps = drps + str(field1[r, c])
                #drps = drps + DROP[field1[r, c]]
            print(drps)
    print("\n")# }}}

def fall_field(field1):# {{{
    fld = field1.copy()
    for r in np.arange(ROW):
        for c in np.arange(COL):
            for k in np.arange(ROW):
                if k+1 > ROW-1:
                    break
                if fld[k+1, c] == 0:
                    fld[k+1, c] = fld[k, c]
                    fld[k, c] = 0
    return fld# }}}

def swap(field1, r1, c1, r2, c2): # waring! zero origin!!  {{{
    fld = field1.copy()
    temp = fld[r1, c1]
    fld[r1, c1] = fld[r2, c2]
    fld[r2, c2] = temp
    return fld# }}}

def operation(field1, route1):# {{{
    fld = field1.copy()
    now_row = route1[0, 0]
    now_col = route1[0, 1]
    #print("now_row:"+str(now_row))
    #print("now_col:"+str(now_col))
    for t in np.arange(MAX_TURN):
        #print("t:"+str(t))
        if route1[t, 0] == -1 or route1[t, 1] == -1:
            break
        fld = swap(fld, now_row, now_col, route1[t, 0], route1[t, 1])
        now_row = route1[t, 0]
        now_col = route1[t, 1]
    return fld# }}}

def chain(field1, chainf, dummyf, now_row, now_col, drop, count):# {{{
    fld = field1.copy()
    global max_count
    if now_row == -1 or now_row == ROW or now_col == -1 or now_col == COL:
        return
    if fld[now_row, now_col] == drop and chainf[now_row, now_col] == 0:
        chainf[now_row, now_col] = -1
        if max_count < count:
            max_count = count
        dummyf[now_row, now_col] = -1

        chain(fld, chainf, dummyf, now_row-1, now_col, drop, count+1)
        chain(fld, chainf, dummyf, now_row+1, now_col, drop, count+1)
        chain(fld, chainf, dummyf, now_row, now_col-1, drop, count+1)
        chain(fld, chainf, dummyf, now_row, now_col+1, drop, count+1)# }}}

# field = set_field(field, "123412341234")
# show_field(field)
# max_count = 0
# chain(field, chainflag, dummy, 0, 3, 3, 0)
# print("max_count:"+str(max_count))
# show_field(chainflag)
# show_field(dummy)

def check(field1, dummyf, t_eracef):# {{{
    fld = field1.copy()
    v = 0
    for r in np.arange(ROW):
        for c in np.arange(COL-2):
            if dummyf[r, c] == -1 and dummyf[r, c+1] == -1 and dummyf[r, c+2] == -1 and fld[r, c] == fld[r, c+1] and fld[r, c] == fld[r, c+2]:
                t_eracef[r, c] = -1
                t_eracef[r, c+1] = -1
                t_eracef[r, c+2] = -1
                v = 1
    for r in np.arange(ROW-2):
        for c in np.arange(COL):
            if dummyf[r, c] == -1 and dummyf[r+1, c] == -1 and dummyf[r+2, c] == -1 and fld[r, c] == fld[r+1, c] and fld[r, c] == fld[r+2, c]:
                t_eracef[r, c] = -1
                t_eracef[r+1, c] = -1
                t_eracef[r+2, c] = -1
                v = 1
    return v# }}}

# field = set_field(field, "123412341234")
# show_field(field)
# chain(field, chainflag, dummy, 0, 0, 0, 0)
# value = check(field, dummy, t_erace)
# print("value:"+str(value))
# show_field(chainflag)
# show_field(dummy)
# show_field(t_erace)

def evaluate(field1):# {{{
    global max_count
    fld = field1.copy()
    value = 0
    chainflag = np.zeros((ROW, COL), dtype=int)
    for r in np.arange(ROW):
        for c in np.arange(COL):
            if chainflag[r, c] == 0 and fld[r, c] != 0:
                max_count = 0
                dummy = np.zeros((ROW, COL), dtype=int)
                chain(fld, chainflag, dummy, r, c, fld[r, c], 1)
                if max_count >= 3:
                    if check(fld, dummy, t_erace) == 1:
                        value += 1
    return value# }}}

# # field = set_field(field, "123412341234")
# field = set_field(field, "123456123456234561654321654321")
# show_field(field)
# value = evaluate(field)
# print("value:"+str(value))
# show_field(chainflag)
# show_field(dummy)
# show_field(t_erace)

def sum_e(field1):# {{{
    global t_erace
    fld = field1.copy()
    combo = 0
    while 1==1:
        a = evaluate(fld)
        # show_field(fld)
        # show_field(t_erace)
        if a == 0:
            break
        for r in np.arange(ROW):
            for c in np.arange(COL):
                if t_erace[r, c] == -1:
                    fld[r, c] = 0
        fld = fall_field(fld)
        combo += a
        t_erace = np.zeros((ROW, COL), dtype=int)
    return combo, fld# }}}

# # field = set_field(field, "123412341234")
# field = set_field(field, "123456125456234561654621654561")
# show_field(field)
# combo, fld = sum_e(field)
# print("combo:"+str(combo))
# show_field(fld)
# show_field(chainflag)
# show_field(dummy)
# show_field(t_erace)


# @jit
def beam_search(field1):  # {{{
    global max_count, t_erace
    # fld = field1.copy()

    que_member = []  # numpy array
    # que_movei = np.full((MAX_TURN, 2), -1, dtype=int)
    # que_member.append([0, 0, 0, -1, que_movei])  # score, nowR, nowC, prev, movei(route)

    for r in np.arange(ROW):
        for c in np.arange(COL):
            que_movei = np.full((MAX_TURN, 2), [r, c], dtype=int)
            que_member.append([0, r, c, -1, que_movei])  # numpy array
    # print("1:len(que_member):"+str(len(que_member)))
    # print("que_member[10]:")
    # print(que_member[10])

    dx = [-1,  0, 0, 1]
    dy = [ 0, -1, 1, 0]
    # max_value = 0
    width = 0

    for i in np.arange(MAX_TURN):
        pque_member = []  # numpy array
        while len(que_member) > 0:
            temp = que_member.pop(0)
            # print("temp:")
            # print(temp)
            # print("after temp, 2:len(que_member):"+str(len(que_member)))
            for j in np.arange(len(dx)):
                cand = []
                cand.append(temp[0])  # score
                cand.append(temp[1])  # nowR
                cand.append(temp[2])  # nowC
                cand.append(temp[3])  # prev
                cand.append(temp[4])  # movei
                # print("j:"+str(j))
                # print("cand:")
                # print(cand)
                if ( 0 <= temp[1]+dy[j] and temp[1]+dy[j] <= ROW-1 and 0 <= temp[2]+dx[j] and temp[2]+dx[j] <= COL-1 ):
                    if cand[3] + j == 3:
                        continue
                    cand[1] = temp[1]+dy[j]
                    cand[2] = temp[2]+dx[j]
                    # print("cand[1]:"+str(cand[1]))
                    # print("cand[2]:"+str(cand[2]))
                    cand[4][i] = [temp[1]+dy[j], temp[2]+dx[j]]
                    # if i > 3:  # loop check movei
                    #     if cand[4][i] == cand[4][i-4]:
                    #         continue
                    route = copy.deepcopy(cand[4])
                    # print("route:")
                    # print(route)
                    fld = operation(field1, route)
                    combo, fld = sum_e(fld)
                    cand[0] = combo
                    cand[3] = j
                    # print("cand[0](combo):")
                    # print(cand[0])
                    # print("cand[3](j):")
                    # print(cand[3])
                    pque_member.append(cand)
                    # print("len(pque_member):"+str(len(pque_member)))
                    # print("3:len(que_member):"+str(len(que_member)))
        pque_member.sort(key=lambda x: x[0], reverse=True)

        # if MAX_TURN < len(pque_member): ,,,,,
        # que_member = copy.deepcopy(pque_member)
        if BEAM_WIDTH <= len(pque_member):
            width = BEAM_WIDTH
        else:
            width = len(pque_member)
        que_member = copy.deepcopy(pque_member[:width])
        # print("4:len(que_member):"+str(len(que_member)))
        # print("que_member[0][0]:"+str(que_member[0][0]))

    best_member = que_member[len(que_member)-1]
    print("best_member:")
    print(best_member)
    best_member = que_member[0]

    return best_member  # }}}


# field = set_field(field, "123456125456234561654621654561")
field = set_field(field)
show_field(field)
best_member = beam_search(field)
route = best_member[4]
print(best_member[0])
print(route)
field = operation(field, route)
combo, field = sum_e(field)
print("combo:"+str(combo))
show_field(field)

def main(field):# {{{
    field = set_field(field)
    show_field(field)
    # field = set_field(field, "123456789012345678901234567890")
    # show_field(field)
    # field = fall_field(field)
    # show_field(field)

    f_field = field.copy()
    best_member = beam_search(field)
    # route = best_member[4]
    # field = operation(f_field, route)
    # print("after operation")
    # show_field(field)
    # combo, field = sum_e(field)
    # print("combo:"+combo)
    # print("after sum_e")
    # show_field(field)# }}}
# if __name__ == '__main__':
#     main(field)
