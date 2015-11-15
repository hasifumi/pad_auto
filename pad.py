# -*- coding: utf-8 -*-

import random
import copy

def create_drops_random(num=30):
    lst = []
    random_srt = "rbgldc"  # r:red, b:blue, g:green, l:light, d:dark, c:cure
    for i in range(num):
        lst.append(random.choice(random_srt))
    return lst

def pivot_drops(drops_lst):
    dct = {}
    for j in drops_lst:
        if j in dct:
            dct[j] += 1
        else:
            dct[j] = 1
    return dct

def sort_drops(pivoted_drops_dct):
    lst = []
    for j in pivoted_drops_dct.keys():
        if len(lst) == 0:
            lst.append([j, pivoted_drops_dct[j]])
        else:
            flg = 0
            for index, value in enumerate(lst):
                if pivoted_drops_dct[j] >= value[1]:
                    lst.insert(index, [j, pivoted_drops_dct[j]])
                    flg = 1
                    break
            if flg == 0:
                lst.append([j, pivoted_drops_dct[j]])
    return lst

def max_combo(pivoted_drops_dct):
    combos = 0
    for k in pivoted_drops_dct.values():
        if k >= 3:
            combos += int(k / 3)
    return combos

def create_goal_drops(sorted_drops_lst, max_combo):
    lst = copy.deepcopy(sorted_drops_lst)
    lst2 = []
    while max_combo >= 1:
        for i in range(len(lst)):
            #print lst[i][0]
            #print lst[i][1]
            #print "max_combo:" + str(max_combo)
            if lst[i][1] >= 3:
                lst2.append(lst[i][0])
                lst2.append(lst[i][0])
                lst2.append(lst[i][0])
                lst[i][1] += -3
                max_combo += -1
    for j in range(len(lst)):
        if lst[j][1] != 0:
            for i in range(lst[j][1]):
                lst2.append(lst[j][0])
    #return [lst, lst2]
    return lst2

#lst = create_drops_random()
#dct = pivot_drops(lst)
#max_cmb = max_combo(dct)
#lst2 = sort_drops(dct)
#lst3 = create_goal_drops(lst2, max_cmb)
#
#print lst
#print dct
#print max_cmb
#print lst2
#print lst3
##print len(lst3[1])
