# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class Node:# {{{
    def __init__(self, start, board):
        self.score = 0
        self.combo = 0
        self.route = []
        self.route.append(start)
        self.board = board

    def set_route(self, lst):
        self.route = lst# }}}

def wrap_search_node_array(args):
    return args[0](*args[1:])

def search_node_array(width, height, max_turn, playnum, parms, node_array, dummy_array):# {{{
    for t in range(max_turn):
        for k in node_array:
            now_pos = k.route[-1]
            if len(k.route) != 1:
                prev_pos = k.route[-2]
            else:
                prev_pos = -1

            for j in get_adjacent(width, now_pos):
                if  j != prev_pos:
                    n = Node(k.route[0], k.board)
                    n.set_route(k.route[:])
                    n.board = swap(now_pos, j, k.board)
                    n.score, n.combo = calc_score(width, height, n.board, parms)
                    n.route.append(j)
                    if len(dummy_array) > playnum:
                        idx = 0
                        worst = 999999
                        for d,v in enumerate(dummy_array):
                            if worst > v.score:
                                worst = v.score
                                idx = d
                        del dummy_array[idx]
                    dummy_array.append(n)

            # i += 1
        node_array = []
        node_array = dummy_array[:]
        dummy_array = []

    return node_array# }}}

def Nbeam(width, height, start_board, max_turn, playnum, parms):# {{{
    node_array = []
    dummy_array = []

    for i in range(width * height):
        n = Node(i, start_board)
        node_array.append(n)

    print "start_board : " + str(start_board)
    print "cpu count: " + str(multiprocessing.cpu_count())
    p = multiprocessing.Pool()
    func_args = []
    for na in node_array:
        #print "na: " + str(na)
        func_args.append((search_node_array, width, height, max_turn, playnum, parms, na, dummy_array))
    #print "func_args: " + str(func_args)
    results = p.map(wrap_search_node_array, func_args)
    print "results :" + str(results)
    #node_array.append(p.map(wrap_search_node_array, func_args))
    #print node_array

    # node_array = search_node_array(width, height, max_turn, playnum, parms, node_array, dummy_array)

    idx = 0
    best = 0
    for k,v in enumerate(node_array):
        if best < v.score:
            best = v.score
            idx = k

    print "best score:" + str(node_array[idx].score)
    print "best combo:" + str(node_array[idx].combo)

    return node_array[idx]# }}}

if __name__ == '__main__':
    from multiprocessing import Pool
    p = Pool()
    func_args = []
    node_array = []
    dummy_array = []

    WIDTH = 6
    HEIGHT = 5

    MAX_TURN = 45
    PLAYNUM = 500

    start_board = "grllggglgrlrgrlrlggrlgggrlllrr"

    DEFAULT_PARMS = {# {{{
            'name'  : "default",
            'red'  : 0.0,
            'blue' : 0.0,
            'green': 0.0,
            'light': 0.0,
            'dark' : 0.0,
            'cure' : 0.0,
            '3colors'  : 0.0,
            '4colors'  : 0.0,
            '5colors'  : 0.0,
            '3colors+cure'  : 0.0,
            '4colors+cure'  : 0.0,
            '5colors+cure'  : 0.0,
            '4drops-red'  : 0.0,
            '4drops-blue' : 0.0,
            '4drops-green': 0.0,
            '4drops-light': 0.0,
            '4drops-dark' : 0.0,
            '4drops-cure' : 0.0,
            '5drops-red'  : 0.0,
            '5drops-blue' : 0.0,
            '5drops-green': 0.0,
            '5drops-light': 0.0,
            '5drops-dark' : 0.0,
            '5drops-cure' : 0.0,
            '1line-red'  : 0.0,
            '1line-blue' : 0.0,
            '1line-green': 0.0,
            '1line-light': 0.0,
            '1line-dark' : 0.0,
            '1line-cure' : 0.0,
            }# }}}

    parms = DEFAULT_PARMS

    for i in range(6 * 5):
        n = Node(i, start_board)
        node_array.append(n)

    print node_array
    for na in node_array:
        #func_args.append((search_node_array, 6, 5, 45, playnum, parms, node_array, dummy_array) )
        func_args.append((search_node_array, 6, 5, 45, 500, parms, na, dummy_array) )

    print func_args
    results = p.map(wrap_search_node_array, func_args)
    print results

#if __name__ == '__main__':
#    from multiprocessing import Pool
#    p = Pool()
#    func_args = []
#    for a in xrange(1,10):
#        for b in xrange(1,10):
#            func_args.append( (myfunc, a, b) )
#    results = p.map(argwrapper, func_args)
#    print results
