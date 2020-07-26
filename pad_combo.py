# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import numpy as np
import random

COL = 6
ROW = 5
MAX_TURN = 10
BEAM_COL = 10
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
f_field = np.zeros((ROW, COL), dtype=int)
chainflg = np.zeros((ROW, COL), dtype=int)
dummy = np.zeros((ROW, COL), dtype=int)
t_erace = np.zeros((ROW, COL), dtype=int)
max_count = 0
route = np.full((MAX_TURN, 2), -1, dtype=int)  # example [[r1 c1], [r2 c2], [r3 c3],,,,]
# print(route)

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

field = set_field(field)
show_field(field)
# field = set_field(field, "123456789012345678901234567890")
# show_field(field)

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

# field = fall_field(field)
# show_field(field)

def swap(field1, r1, c1, r2, c2): # waring! zero origin!!  {{{
    fld = field1.copy()
    temp = fld[r1, c1]
    fld[r1, c1] = fld[r2, c2]
    fld[r2, c2] = temp
    return fld# }}}

# field = swap(field, 0, 0, 1, 0)
# show_field(field)

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

# route[0] = [0, 0]
# route[1] = [0, 1]
# route[2] = [1, 1]
# route[3] = [1, 2]
# print(route)
# field = operation(field, route)
# show_field(field)

def chain(field1, now_row, now_col, drop, count):
    fld = filed1.copy()
    if now_row == -1 or now_row  > ROW or now_col == -1 now_col > COL:


#    if length(ARGS) >= 2{{{
#        COL=parse(Int, ARGS[2])
#    end
#    if length(ARGS) >= 3
#        ROW=parse(Int, ARGS[3])
#    end
#    if length(ARGS) >= 4
#        eval_param=parse(Int, ARGS[4])
#    end}}}
#
#    mutable struct member#={{{=#
#        score::Int8
#        nowR::Int8
#        nowC::Int8
#        prev::Int8
#        movei
#    end#=}}}=#
#
#    function sort_member(a, b)#={{{=#
#        if a.score < b.score
#            return true
#        end
#        return false
#    end#=}}}=#
#
#    # sort example{{{{{{
#    #    m1 = member(1, 1, 3, 4, [1 1; 2 2;])
#    #    m2 = member(3, 2, 3, 4, [])
#    #    m3 = member(2, 3, 3, 4, [])
#    #    arr_member = Array{member}(undef, 3)
#    #    arr_member[1] = m1
#    #    arr_member[2] = m2
#    #    arr_member[3] = m3
#    #    sort!(arr_member, lt=sort_member, rev=true)
#    #}}}}}}
#
#    function chain(now_row, now_col, drop, count)#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        if now_row == 0 || now_row > ROW || now_col == 0 || now_col > COL
#            return
#        end
#        if field[now_row, now_col] == drop && chainflag[now_row, now_col] == 0
#            global chainflag[now_row, now_col] = -1
#            if max_count < count
#                global max_count = count
#            end
#            global dummy[now_row, now_col] = -1
#
#            chain(now_row-1, now_col, drop, count+1)
#            chain(now_row+1, now_col, drop, count+1)
#            chain(now_row, now_col-1, drop, count+1)
#            chain(now_row, now_col+1, drop, count+1)
#        end
#    end#=}}}=#
#
#    function evaluate()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        value = 0
#        chainflag = zeros(Int8, ROW, COL)
#        for i in 1:ROW
#            flg_row = 0
#            for j in 1:COL
#                if chainflag[i, j] == 0 && field[i, j] != 0
#                    global max_count = 0
#                    global dummy = zeros(Int8, ROW, COL)
#                    chain(i, j, field[i, j], 1)
#                    if max_count >= 3
#                        if check() == 1
#                            value += 1
#                        end
#                    end
#                end
#                if j <= COL-1
#                    if field[i, j] != 0 && field[i, j] == field[i, j+1]
#                        flg_row += 1
#                        #println("flg_row:", flg_row)
#                    end
#                end
#            end
#            if flg_row == COL-1
#                value += 10
#            end
#        end
#        return value
#    end#=}}}=#
#
#    function check()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        v = 0
#        for i in 1:ROW
#            for j in 1:COL-2
#                if dummy[i, j] == -1 && dummy[i, j+1] == -1 && dummy[i, j+2] == -1 && field[i, j] == field[i, j+1] && field[i, j] == field[i, j+2]
#                    global t_erace[i, j] = -1
#                    global t_erace[i, j+1] = -1
#                    global t_erace[i, j+2] = -1
#                    v = 1
#                end
#            end
#        end
#
#        for i in 1:ROW-2
#            for j in 1:COL
#                if dummy[i, j] == -1 && dummy[i+1, j] == -1 && dummy[i+2, j] == -1 && field[i, j] == field[i+1, j] && field[i, j] == field[i+2, j]
#                    global t_erace[i, j] = -1
#                    global t_erace[i+1, j] = -1
#                    global t_erace[i+2, j] = -1
#                    v = 1
#                end
#            end
#        end
#        return v
#    end#=}}}=#
#
#    function sum_e()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        combo = 0
#        while(1==1)
#            global t_erace = zeros(Int8, ROW, COL)
#            a = evaluate()
#            if a == 0
#                break
#            end
#            for i in 1:ROW
#                for j in 1:COL
#                    if t_erace[i, j] == -1
#                        global field[i, j] = 0
#                    end
#                end
#            end
#            fall()
#            combo += a
#        end
#        return combo
#    end#=}}}=#
#
#    function check_delete_row()
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        count_row = 0
#        for i in 1:ROW
#            flg_row = 0
#            for j in 1:COL
#                if j <= COL-1
#                    if field[i, j] != 0 && field[i, j] == field[i, j+1]
#                        flg_row += 1
#                        #println("flg_row:", flg_row)
#                    end
#                end
#            end
#            if flg_row == COL-1
#                count_row += 1
#            end
#        end
#        return count_row * 5
#    end
#
#    function add_evaluate(score, eval_param="")
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        new_score = score
#        if length(eval_param) != 0
#            #println("length(eval_param):", length(eval_param))
#            field = copy(f_field)
#            operation()
#            if eval_param[1] == "1"   # if flg_delete_row is on("1") then ...
#                new_score += check_delete_row()
#            end
#        end
#        #println("new_score:", new_score)
#        return new_score
#    end
#
#    function beam_search()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#
#        que_member = member[]
#        temp_que = member[]
#        i = 1
#        for i in 1:ROW
#            for j in 1:COL
#                cand = member(0, i, j, -1, [])
#                cand.movei = fill(-1, MAX_TURN, 2)
#                cand.movei[1, :] = [i j]
#                push!(que_member, cand)
#            end
#        end
#        #println("size(que_member, 1):", size(que_member, 1))
#        #println("que_member[1]:", que_member[1])
#
#        dx = [-1;  0; 0; 1]
#        dy = [ 0; -1; 1; 0]
#        max_value = 0
#        width = 0
#
#        for i in 1:MAX_TURN
#            #pque_member = Array{member}(undef, 1)
#            pque_member = member[]
#            while length(que_member) != 0
#                #temp = pop!(que_member)
#                temp = que_member[1]
#                #println("before length(que_member)", length(que_member))
#                temp_que = copy(que_member[2:end])
#                que_member = copy(temp_que)
#                #println("after length(que_member)", length(que_member))
#                #println("temp:", temp)
#                for j in 1:length(dx)
#                    field = copy(f_field)
#                    cand = member(0, i, j, -1, [])
#                    cand.score = temp.score
#                    cand.nowC = temp.nowC
#                    cand.nowR = temp.nowR
#                    cand.prev = temp.prev
#                    cand.movei = copy(temp.movei)
#                    if ( 1 <= temp.nowC + dx[j] <= COL && 1 <= temp.nowR + dy[j] <= ROW )
#                        if cand.prev + j == 5
#                            continue
#                        end
#                        cand.nowC = temp.nowC + dx[j]
#                        cand.nowR = temp.nowR + dy[j]
#                        #cand.movei[i, :] = [cand.nowC cand.nowR;]
#                        cand.movei[i, :] = [temp.nowC+dx[j] temp.nowR+dy[j]]
#                        if i > 4
#                            if cand.movei[i, :] == cand.movei[i-4, :]
#                            #     println("cand.movei[i, :]:", cand.movei[i, :])
#                            #     println("cand.movei[i-4, :]:", cand.movei[i-4, :])
#                                continue
#                            end
#                            # println("cand.movei:", cand.movei)
#                            # println("i:", i)
#                            # println("length(cand.movei):", length(cand.movei))
#                            # println("cand.movei[i, :]:", cand.movei[i, :])
#                            # println("cand.movei[i-3, :]:", cand.movei[i-3, :])
#                        end
#                        #println("temp.nowC:", temp.nowC, ", temp.nowR:", temp.nowR, ", dx[j]:", dx[j], ", dy[j]:", dy[j])
#                        #println("temp.nowC + dx[j]:", temp.nowC + dx[j])
#                        #println("temp.nowR + dy[j]:", temp.nowR + dy[j])
#                        #println("cand.movei[i, :] in beam_search:", cand.movei[i, :])
#                        route = copy(cand.movei)
#                        #println("route in beam_search:", route)
#                        operation()
#                        cand.score = sum_e()
#                        temp_score = cand.score
#                        cand.score = add_evaluate(temp_score, eval_param)
#                        #println("cand.score in beam_search:", cand.score)
#                        cand.prev = j
#                        push!(pque_member, cand)
#                    end
#                end
#            end
#            sort!(pque_member, lt=sort_member, rev=true)
#
#            if MAX_TURN < length(pque_member)
#                width = MAX_TURN
#            else
#                width = length(pque_member)
#            end
#            que_member = Array{member}(undef, width)
#            que_member[1:width, : ] = pque_member[1:width, : ]
#        end
#
#        #println(que_member[1:10, : ])
#        return que_member[1]  # return best_member
#
#        best_member = que_member[1]
#        return best_member
#    end#=}}}=#
#
#    function main()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#    	#set()
#        set("315211554451322114424566531621")  # 15 combo
#        println("initial field.")
#        global field, f_field, route
#        show(field)
#        f_field = copy(field)
#        #route[1:6 , : ] = [1 1; 2 1; 3 1; 4 1; 5 1; 6 1;]
#        #print(route[1:6, :], "\n")
#
#        #best_member = member()
#        best_member = beam_search()
#        println("best_member:",  best_member)
#        #println(size(best_member.movei, 1))
#        route[1:size(best_member.movei, 1), : ] = best_member.movei
#        #println("route:",  route)
#        field = copy(f_field)
#        operation()
#        println("after operation")
#        show(field)
#        combo = sum_e()
#        println("combo:", combo)
#        println("after sum_e")
#        show(field)
#    end#=}}}=#
#
#    function get_args()#={{{=#
#        println(length(ARGS))
#        if length(ARGS) > 0
#            println(ARGS)
#            for x in ARGS
#                println(x)
#            end
#        end
#    end#=}}}=#
#
#    function main1()#={{{=#
#        global field, f_field, chainflag, dummy, t_erace, max_count, route
#        # get_args()
#        set(ARGS[1])
#        global field, f_field, route
#        # show(field)
#        f_field = copy(field)
#        best_member = beam_search()
#
#        # println("best_member:",  best_member)
#        # route[1:size(best_member.movei, 1), : ] = best_member.movei
#        # field = copy(f_field)
#        # operation()
#        # println("after operation")
#        # show(field)
#        # combo = sum_e()
#        # println("combo:", combo)
#        # println("after sum_e")
#        # show(field)
#
#        # mvi = string(best_member.movei[1, 1]) * "," * string(best_member.movei[1, 2])
#        # println(mvi)
#        # println(length(best_member.movei))
#
#        for b in 1:MAX_TURN
#            #print(b)
#            println(string(best_member.movei[b, 1]) * "," * string(best_member.movei[b, 2]))
#        end
#    end#=}}}=#
#
#    # main()
#    # get_args()
#
#    main1()
#
#
