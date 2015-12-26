# -*- coding: utf-8 -*-

#def chkdrops4(self):
def chkdrops4(combo):
    drops4 = {}
    #for k in self.combo:
    for k in combo:
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
            #print temp_k
            drops4[k[5]] = temp_k
        #print drops4
    for v in drops4.keys():
        if drops4[v][3] == "h" and drops4[v][2] != 1:
            del drops4[v]
        elif drops4[v][3] == "v" and drops4[v][1] != 1:
            del drops4[v]
    return drops4

    # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
    #[[0, 0, 0, 'h', 'r', 0], [1, 1, 0, 'h', 'r', 0], [2, 2, 0, 'h', 'r', 0], [3, 3, 0, 'h', 'r', 0], [4, 0, 1, 'h', 'b', 1], [5, 1, 1, 'h', 'b', 1], [6, 2, 1, 'h', 'b', 1], [7, 3, 1, 'h', 'b', 1], [8, 3, 2, 'h', 'g', 8], [9, 0, 3, 'h', 'd', 9], [10, 0, 4, 'h', 'c', 4], [11, 1, 4, 'h', 'c', 4], [12, 2, 4, 'h', 'c', 4], [13, 3, 4, 'h', 'c', 4]]

combo = [[0, 0, 0, 'h', 'r', 0], [1, 1, 0, 'h', 'r', 0], [4, 0, 1, 'h', 'b', 1], [5, 1, 1, 'h', 'b', 1], [8, 3, 2, 'h', 'g', 8], [9, 0, 3, 'h', 'd', 9]]

drops4 = chkdrops4(combo)
print drops4
