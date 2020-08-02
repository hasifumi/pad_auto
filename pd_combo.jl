# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

ROW = 5
COL = 6
MAX_TURN = 50
BEAM_WIDTH = 800
# MAX_TURN = 5
# BEAM_WIDTH = 5
eval_param = 0

if length(ARGS) >= 2
    COL=parse(Int, ARGS[2])
end
if length(ARGS) >= 3
    ROW=parse(Int, ARGS[3])
end
if length(ARGS) >= 4
    debug_flg=parse(Int, ARGS[4])
end
if length(ARGS) >= 5
    eval_param=ARGS[5]
end
# println(COL)
# println(ROW)


field = zeros(Int8, ROW, COL)
f_field = zeros(Int8, ROW, COL)
chainflag = zeros(Int8, ROW, COL)
dummy = zeros(Int8, ROW, COL)
t_erace = zeros(Int8, ROW, COL)
max_count = 0
route = fill(-1, MAX_TURN, 2)

mutable struct member#={{{=#
    score::Int8
    nowR::Int8
    nowC::Int8
    prev::Int8
    movei
end#=}}}=#

function sort_member(a, b)#={{{=#
    if a.score < b.score
        return true
    end
    return false
end#=}}}=#

# sort example{{{{{{
#    m1 = member(1, 1, 3, 4, [1 1; 2 2;])
#    m2 = member(3, 2, 3, 4, [])
#    m3 = member(2, 3, 3, 4, [])
#    arr_member = Array{member}(undef, 3)
#    arr_member[1] = m1
#    arr_member[2] = m2
#    arr_member[3] = m3
#    sort!(arr_member, lt=sort_member, rev=true)
#}}}}}}

function set(field1=[])#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    if length(field1) < 12
	    for i in 1:ROW
	    	for j in 1:COL
	    		if field[i, j] == 0
	    			field[i, j] = rand(1:6)
	    			field[i, j] = rand(1:5)
	    		end
	    	end
	    end
    else
	    for i in 1:ROW
	    	for j in 1:COL
                w = (i-1)*COL+j
                field[i, j] = parse(Int8, field1[(i-1)*COL+j])
	    	end
	    end
    end
end#=}}}=#

function show(field)#={{{=#
    for i in 1:ROW
        for j in 1:COL
            print(field[i, j])
        end
        print("\n")
    end
end#=}}}=#

function fall()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    for i in 1:ROW
        for j in 1:COL
            for k in 1:ROW
                if k+1 > ROW
                    break
                end
                if field[k+1, j] == 0
                    global field[k+1, j] = field[k, j]
                    global field[k, j] = 0
                end
            end
        end
    end
end#=}}}=#

function swap(i1, j1, i2, j2)#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    temp = field[i1, j1]
    global field[i1, j1] = field[i2, j2]
    global field[i2, j2] = temp
end#=}}}=#

function operation()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    now_col = route[1, 2]
    now_row = route[1, 1]
    #print("now_col" , now_col , ", now_row:" , now_row, "\n")

    for i in 1:MAX_TURN
        if route[i, 1] == -1 || route[i, 2] == -1
            break
        end
        swap(now_col, now_row, route[i, 2], route[i, 1])
        now_col = route[i, 2]  # x position
        now_row = route[i, 1]  # y position
    end
end#=}}}=#

function chain(now_row, now_col, drop, count)#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    if now_row == 0 || now_row > ROW || now_col == 0 || now_col > COL
        return
    end
    if field[now_row, now_col] == drop && chainflag[now_row, now_col] == 0
        global chainflag[now_row, now_col] = -1
        if max_count < count
            global max_count = count
        end
        global dummy[now_row, now_col] = -1

        chain(now_row-1, now_col, drop, count+1)
        chain(now_row+1, now_col, drop, count+1)
        chain(now_row, now_col-1, drop, count+1)
        chain(now_row, now_col+1, drop, count+1)
    end
end#=}}}=#

function evaluate()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    value = 0
    chainflag = zeros(Int8, ROW, COL)
    for i in 1:ROW
        flg_row = 0
        for j in 1:COL
            if chainflag[i, j] == 0 && field[i, j] != 0
                global max_count = 0
                global dummy = zeros(Int8, ROW, COL)
                chain(i, j, field[i, j], 1)
                if max_count >= 3
                    if check() == 1
                        value += 1
                    end
                end
            end
            # if j <= COL-1
            #     if field[i, j] != 0 && field[i, j] == field[i, j+1]
            #         flg_row += 1
            #         #println("flg_row:", flg_row)
            #     end
            # end
        end
        # if flg_row == COL-1
        #     value += 10
        # end
    end
    return value
end#=}}}=#

function check()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    v = 0
    for i in 1:ROW
        for j in 1:COL-2
            if dummy[i, j] == -1 && dummy[i, j+1] == -1 && dummy[i, j+2] == -1 && field[i, j] == field[i, j+1] && field[i, j] == field[i, j+2]
                global t_erace[i, j] = -1
                global t_erace[i, j+1] = -1
                global t_erace[i, j+2] = -1
                v = 1
            end
        end
    end

    for i in 1:ROW-2
        for j in 1:COL
            if dummy[i, j] == -1 && dummy[i+1, j] == -1 && dummy[i+2, j] == -1 && field[i, j] == field[i+1, j] && field[i, j] == field[i+2, j]
                global t_erace[i, j] = -1
                global t_erace[i+1, j] = -1
                global t_erace[i+2, j] = -1
                v = 1
            end
        end
    end
    return v
end#=}}}=#

function analyze_board(field1)#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    cnt_drops = zeros(Int8, 6)  # number of drops ( 1:red, 2:blue, 3:green, 4:light, 5:dark, 6:cure )

    for i in 1:length(field1)
        cnt_drops[field1[i]] += 1
    end
    for i in 1:length(cnt_drops)
        println("cnt_drops["*string(i)*"]:", cnt_drops[i])
    end
    c = findfirst(x->x==maximum(cnt_drops), cnt_drops)
    println("color index of max drops:"*string(c)*", max:"*string(cnt_drops[c]))
    cnt_drops[c] = cnt_drops[c] - 5
    println("L-ji:"*string(c)*", remaining:"*string(cnt_drops[c]))

    cnt_cmbs = map(x-> Int(floor(x/3)), cnt_drops)
    for i in 1:length(cnt_cmbs)
        println("cnt_cmbs["*string(i)*"]:", cnt_cmbs[i])
    end
    sum_cmbs = sum(cnt_cmbs)+1
    println("sum combo(add L-ji):"*string(sum_cmbs))

end#=}}}=#

function sum_e()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    combo = 0
    while(1==1)
        global t_erace = zeros(Int8, ROW, COL)
        a = evaluate()
        if a == 0
            break
        end
        for i in 1:ROW
            for j in 1:COL
                if t_erace[i, j] == -1
                    global field[i, j] = 0
                end
            end
        end
        fall()
        combo += a
    end
    return combo
end#=}}}=#

function check_delete_row()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    count_row = 0
    for i in 1:ROW
        flg_row = 0
        for j in 1:COL-1
            if field[i, j] != field[i, j+1]
                flg_row = 1
            end
        end
        if flg_row == 0
            count_row += 1
        end
    end
    # println("count_row:", count_row)
    return count_row * 6
end#=}}}=#

function check_l_ji()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    count_l_ji = 0
    for i in 1:ROW
        for j in 1:COL
            if i > 2 && j+2 <= COL # case " |_ " #={{{=#

                if ( field[i, j] == field[i, j+1] == field[i, j+2] ) && ( field[i, j] == field[i-1, j] == field[i-2, j] )
                    flg_ng = 0
                    if  i > 3
                        if ( field[i, j] == field[i-3, j] )
                            flg_ng = 1
                        end
                    end
                    if i+1 <= ROW
                        if (field[i, j] == field[i+1, j]) || ((field[i, j] == field[i+1, j+1]) && (field[i, j] == field[i-1, j+1])) || ((field[i, j] == field[i+1, j+2] ) && (field[i, j] == field[i-1, j+2]))
                            flg_ng = 1
                        end
                    end
                    if j+3 <= COL
                        if ( field[i, j] == field[i, j+3] )
                            flg_ng = 1
                        end
                    end
                    if j > 1
                        if ( field[i, j] == field[i, j-1] ) || ((field[i, j] == field[i-1, j-1]) && (field[i, j] == field[i-1, j+1])) || ((field[i, j] == field[i-2, j-1]) && (field[i, j] == field[i-2, j+1]))
                            flg_ng = 1
                        end
                    end
                    if flg_ng == 0
                        count_l_ji += 1
                    end
                end
            end#=}}}=#

            if i+2 <= ROW && j+2 <= COL # case " |- " #={{{=#

                if ( field[i, j] == field[i, j+1] == field[i, j+2] ) && ( field[i, j] == field[i+1, j] == field[i+2, j] )
                    flg_ng = 0
                    if  i+3 <= ROW
                        if ( field[i, j] == field[i+3, j] )
                            flg_ng = 1
                        end
                    end
                    if i > 1
                        if (field[i, j] == field[i-1, j]) || ((field[i, j] == field[i-1, j+1]) && (field[i, j] == field[i+1, j+1])) || ((field[i, j] == field[i-1, j+2] ) && (field[i, j] == field[i+1, j+2]))
                            flg_ng = 1
                        end
                    end
                    if j+3 <= COL
                        if ( field[i, j] == field[i, j+3] )
                            flg_ng = 1
                        end
                    end
                    if j > 1
                        if ( field[i, j] == field[i, j-1] ) || ((field[i, j] == field[i+1, j-1]) && (field[i, j] == field[i+1, j+1])) || ((field[i, j] == field[i+2, j-1]) && (field[i, j] == field[i+2, j+1]))
                            flg_ng = 1
                        end
                    end
                    if flg_ng == 0
                        count_l_ji += 1
                    end
                end
            end#=}}}=#

            if i+2 <= ROW && j+2 <= COL # case " -| " #={{{=#

                if ( field[i, j] == field[i, j+1] == field[i, j+2] ) && ( field[i, j] == field[i+1, j+2] == field[i+2, j+2] )
                    flg_ng = 0
                    if  i+3 <= ROW
                        if ( field[i, j] == field[i+3, j+2] )
                            flg_ng = 1
                        end
                    end
                    if i > 1
                        if (field[i, j] == field[i-1, j+2]) || ((field[i, j] == field[i-1, j]) && (field[i, j] == field[i+1, j])) || ((field[i, j] == field[i-1, j+1] ) && (field[i, j] == field[i+1, j+1]))
                            flg_ng = 1
                        end
                    end
                    if j > 1
                        if ( field[i, j] == field[i, j-1] )
                            flg_ng = 1
                        end
                    end
                    if j+3 <= COL
                        if ( field[i, j] == field[i, j+3] ) || ((field[i, j] == field[i+1, j+1]) && (field[i, j] == field[i+1, j+3])) || ((field[i, j] == field[i+2, j+1]) && (field[i, j] == field[i+2, j+3]))
                            flg_ng = 1
                        end
                    end
                    if flg_ng == 0
                        count_l_ji += 1
                    end
                end
            end#=}}}=#

            if i > 2 && j+2 <= COL # case " _| " #={{{=#

                if ( field[i, j] == field[i, j+1] == field[i, j+2] ) && ( field[i, j] == field[i-1, j+2] == field[i-2, j+2] )
                    flg_ng = 0
                    if  i > 3
                        if ( field[i, j] == field[i-3, j+2] )
                            flg_ng = 1
                        end
                    end
                    if i+1 <= ROW
                        if (field[i, j] == field[i+1, j+2]) || ((field[i, j] == field[i+1, j]) && (field[i, j] == field[i-1, j])) || ((field[i, j] == field[i+1, j+1] ) && (field[i, j] == field[i-1, j+1]))
                            flg_ng = 1
                        end
                    end
                    if j > 1
                        if ( field[i, j] == field[i, j-1] )
                            flg_ng = 1
                        end
                    end
                    if j+3 <= COL
                        if ( field[i, j] == field[i, j+3] ) || ((field[i, j] == field[i-1, j+1]) && (field[i, j] == field[i-1, j+3])) || ((field[i, j] == field[i-2, j+1]) && (field[i, j] == field[i-2, j+3]))
                            flg_ng = 1
                        end
                    end
                    if flg_ng == 0
                        count_l_ji += 1
                    end
                end
            end#=}}}=#

        end
    end
    if count_l_ji == 0
        return 0
    else
        return 10
    end
    # return count_l_ji * 5
end#=}}}=#

function check_delete_col()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    count_col = 0
    for j in 1:COL
        flg_col = 0
        for i in 1:ROW
            if field[i, j] != 6  # 6:cure && "oiuchi"
                flg_col = 1
                # println("break j:", j)
                # break
            end
            if i+1 <= ROW
                if field[i, j] != field[i+1, j]
                    flg_col = 1
                end
            end
            if j+2 <= COL
                if (field[i, j] == field[i, j+1]) && (field[i, j] == field[i, j+2])
                    flg_col = 1
                end
            end
            if j > 1 && j+1 <= COL
                if (field[i, j] == field[i, j-1]) && (field[i, j] == field[i, j+1])
                    flg_col = 1
                end
            end
            if j > 2
                if (field[i, j] == field[i, j-1]) && (field[i, j] == field[i, j-2])
                    flg_col = 1
                end
            end
        end
        if flg_col == 0
            count_col += 1
            # println("j:", j)
            # println("count_col:", count_col)
        end
    end
    # println("count_col:", count_col)
    return count_col * 5
end#=}}}=#

function add_evaluate(score, eval_param="")#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
    # println("add_evaluate")
    # println("eval_param:", eval_param)
    # println("eval_param[2]:", eval_param[2])
    # println("typeof(eval_param[2]):", typeof(eval_param[2]))
    new_score = score
    if length(eval_param) != 0
        #println("length(eval_param):", length(eval_param))
        field = copy(f_field)
        operation()
        if eval_param[1] == '1'   # if flg_delete_row is on('1') then ...
            new_score += check_delete_row()
        end
        if eval_param[2] == '1'   # if flg_l_ji is on('1') then ...
            # println("check_l_ji()")
            new_score += check_l_ji()
        end
        if eval_param[3] == '1'   # if flg_delete_col is on('1') then ...
            new_score += check_delete_col()
        end
    end
    return new_score
end#=}}}=#

function beam_search()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route

    que_member = member[]
    temp_que = member[]
    i = 1
    for i in 1:ROW
        for j in 1:COL
            cand = member(0, i, j, -1, [])
            cand.movei = fill(-1, MAX_TURN, 2)
            cand.movei[1, :] = [i j]
            push!(que_member, cand)
        end
    end
    #println("size(que_member, 1):", size(que_member, 1))
    #println("que_member[1]:", que_member[1])

    dx = [-1;  0; 0; 1]
    dy = [ 0; -1; 1; 0]
    max_value = 0
    width = 0

    for i in 1:MAX_TURN
        #pque_member = Array{member}(undef, 1)
        pque_member = member[]
        while length(que_member) != 0
            #temp = pop!(que_member)
            temp = que_member[1]
            #println("before length(que_member)", length(que_member))
            temp_que = copy(que_member[2:end])
            que_member = copy(temp_que)
            #println("after length(que_member)", length(que_member))
            #println("temp:", temp)
            for j in 1:length(dx)
                field = copy(f_field)
                cand = member(0, i, j, -1, [])
                cand.score = temp.score
                cand.nowC = temp.nowC
                cand.nowR = temp.nowR
                cand.prev = temp.prev
                cand.movei = copy(temp.movei)
                if ( 1 <= temp.nowC + dx[j] <= COL && 1 <= temp.nowR + dy[j] <= ROW )
                    if cand.prev + j == 5
                        continue
                    end
                    cand.nowC = temp.nowC + dx[j]
                    cand.nowR = temp.nowR + dy[j]
                    #cand.movei[i, :] = [cand.nowC cand.nowR;]
                    cand.movei[i, :] = [temp.nowC+dx[j] temp.nowR+dy[j]]
                    if i > 4
                        if cand.movei[i, :] == cand.movei[i-4, :]
                        #     println("cand.movei[i, :]:", cand.movei[i, :])
                        #     println("cand.movei[i-4, :]:", cand.movei[i-4, :])
                            continue
                        end
                        # println("cand.movei:", cand.movei)
                        # println("i:", i)
                        # println("length(cand.movei):", length(cand.movei))
                        # println("cand.movei[i, :]:", cand.movei[i, :])
                        # println("cand.movei[i-3, :]:", cand.movei[i-3, :])
                    end
                    #println("temp.nowC:", temp.nowC, ", temp.nowR:", temp.nowR, ", dx[j]:", dx[j], ", dy[j]:", dy[j])
                    #println("temp.nowC + dx[j]:", temp.nowC + dx[j])
                    #println("temp.nowR + dy[j]:", temp.nowR + dy[j])
                    #println("cand.movei[i, :] in beam_search:", cand.movei[i, :])
                    route = copy(cand.movei)
                    #println("route in beam_search:", route)
                    operation()
                    cand.score = sum_e()
                    temp_score = cand.score
                    cand.score = add_evaluate(temp_score, eval_param)
                    #println("cand.score in beam_search:", cand.score)
                    cand.prev = j
                    push!(pque_member, cand)
                end
            end
        end
        sort!(pque_member, lt=sort_member, rev=true)

        if BEAM_WIDTH < length(pque_member)
            width = BEAM_WIDTH
        else
            width = length(pque_member)
        end
        que_member = Array{member}(undef, width)
        que_member[1:width, : ] = pque_member[1:width, : ]
    end

    #println(que_member[1:10, : ])
    return que_member[1]  # return best_member

    best_member = que_member[1]
    return best_member
end#=}}}=#

function main()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route
	#set(0)
    set("315211554451322114424566531621")  # 15 combo
    println("initial field.")
    global field, f_field, route
    show(field)
    f_field = copy(field)
    #route[1:6 , : ] = [1 1; 2 1; 3 1; 4 1; 5 1; 6 1;]
    #print(route[1:6, :], "\n")

    #best_member = member()
    best_member = beam_search()
    println("best_member:",  best_member)
    #println(size(best_member.movei, 1))
    route[1:size(best_member.movei, 1), : ] = best_member.movei
    #println("route:",  route)
    field = copy(f_field)
    operation()
    println("after operation")
    show(field)
    combo = sum_e()
    println("combo:", combo)
    println("after sum_e")
    show(field)
end#=}}}=#

function get_args()#={{{=#
    println(length(ARGS))
    if length(ARGS) > 0
        println(ARGS)
        for x in ARGS
            println(x)
        end
    end
end#=}}}=#

function main1()#={{{=#
    global field, f_field, chainflag, dummy, t_erace, max_count, route, debug_flg
    # get_args()
    # print(ARGS[1])
    set(ARGS[1])
    global field, f_field, route

    if debug_flg != 0
        show(field)
    end

    f_field = copy(field)

    if debug_flg == 1
        @time best_member = beam_search()
        println("best_member:",  best_member)
        route[1:size(best_member.movei, 1), : ] = best_member.movei
        field = copy(f_field)
        operation()
        println("after operation")
        show(field)
        combo = sum_e()
        combo = add_evaluate(combo, eval_param)
        println("combo:", combo)
        println("after sum_e")
        show(field)
    elseif  debug_flg == 2
        combo = sum_e()
        combo = add_evaluate(combo, eval_param)
        println("combo:", combo)
        println("after sum_e")
        show(field)
    elseif  debug_flg == 3
        analyze_board(field)
    else
        best_member = beam_search()
    end

    # mvi = string(best_member.movei[1, 1]) * "," * string(best_member.movei[1, 2])
    # println(mvi)
    # println(length(best_member.movei))

    if debug_flg == 0
        for b in 1:MAX_TURN
            #print(b)
            println(string(best_member.movei[b, 1]) * "," * string(best_member.movei[b, 2]))
        end
    end

end#=}}}=#

# main()
# get_args()

main1()

