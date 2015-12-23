# -*- coding: utf-8 -*-

import random
import copy

def create_drops_random(w=6, h=5, d="rbgldc"):
    lst = []
    #random_srt = "rbgldc"  # r:red, b:blue, g:green, l:light, d:dark, c:cure
    for i in range(w*h):
        #lst.append(random.choice(random_srt))
        lst.append(random.choice(d))
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

def isEqual_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    if len(lst1) == 0:
        return False
    ret = True
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            ret = False
            break
    return ret

adjacent_3x2 = ((1, 3),         # 0
                (0, 2, 4),      # 1
                (1, 5),         # 2
                (0, 4),         # 3
                (1, 3, 5),      # 4
                (2, 4))         # 5

def exchange(lst, ex1, ex2):  # 0:first_item
    if len(lst) == 0:
        return lst
    if (ex1 + 1 > len(lst)) or (ex2 + 1 > len(lst)):
        return lst
    if ex1 == ex2:
        return lst
    tmp_lst = lst[:]
    tmp = tmp_lst[ex1]
    tmp_lst[ex1] = tmp_lst[ex2]
    tmp_lst[ex2] = tmp
    return tmp_lst



def search(goal_drops, path, prev_drops, adjacent):
    if isEqual_list(goal_drops, prev_drops):
        print path
        print prev_drops
        return
    n = path[len(path) - 1]
    for x in adjacent[n]:
        if x not in path:
            #print "n:" + str(n) + ", x:" + str(x) + ", path:" + str(path)
            ##print "prev_drops[n]:" + str(prev_drops[n]) + ", prev_drops[x]:" + str(prev_drops[x])
            #print "prev_drops:" + str(prev_drops) + ", next_drops:" + str(exchange(prev_drops, x, n))
            path.append(x)
            search(goal_drops, path, exchange(prev_drops, x, n), adjacent)
            path.pop()


#lst = create_drops_random(4, 3, "bgr")
#lst = create_drops_random(d="123456")
#dct = pivot_drops(lst)
#max_cmb = max_combo(dct)
#lst2 = sort_drops(dct)
#lst3 = create_goal_drops(lst2, max_cmb)
#
#print lst
#print "".join(lst)
#print len(lst)
#print dct
#print max_cmb
#print lst2
#print lst3
##print len(lst3[1])

#lst1 = "abc"
#lst2 = "abc"
#print isEqual_list(lst1, lst2)

#lst1 = ["a", "b", "a", "c", "a", "a"]
#lst2 = ["a", "c", "b", "a", "a", "a"]
#
#for x in range(len(lst2)):
#    search(lst1, [x], lst1, adjacent_3x2)

#print exchange(["a", "b", "c", "d", "e"], 3, 2)
