# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_combo
import multiprocessing as mp
import itertools

class Node:# {{{
    def __init__(self, start, board):
        self.score = 0
        self.combo = 0
        self.route = []
        self.route.append(start)
        self.board = board

    def set_route(self, lst):
        self.route = lst# }}}

class Searcher():
    def __init__(self, game_parms, score_parms, search_parms, board):# {{{
        self.game_parms = game_parms
        self.score_parms = score_parms
        self.search_parms = search_parms
        self.board = board
        self.adjacent = self.make_adjacent()
        # }}}

    def xy2idx(self, x, y):# {{{
        return y*self.game_parms.width+x
        # }}}

    def make_adjacent(self):# {{{
        ary = []
        for h in range(self.game_parms.height):
            for w in range(self.game_parms.width):
                ary_b = []
                if 0 <= w - 1:
                    ary_b.append(self.xy2idx(w - 1, h))
                if w + 1 < self.game_parms.width:
                    ary_b.append(self.xy2idx(w + 1, h))
                if 0 <= h - 1:
                    ary_b.append(self.xy2idx(w, h - 1))
                if h + 1 < self.game_parms.height:
                    ary_b.append(self.xy2idx(w, h + 1))
                ary.append(ary_b)
        return ary
        # }}}

    def get_adjacent(self, now_pos):# {{{
        return self.adjacent[now_pos]
        # }}}

    def swap(self, a, b, board):# {{{
        i = int(a)
        j = int(b)
        if i > j:
            temp = i
            i = j
            j = temp
        li = list(board)
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
        temp_board = "".join(li)
        return temp_board
        # }}}

    def calc_score(self, board):# {{{
        combo = pad_combo.PadCombo(self.game_parms.width, \
                                       self.game_parms.height, \
                                       board, \
                                       self.score_parms)
        combo.check_erasable()
        combo.calc_combo()
        return combo.calc_score(self.score_parms)
        # }}}

    def search_node_array(self, node_i):# {{{
        node_array = []
        dummy_array = []

        n = Node(node_i, self.board)
        node_array.append(n)

        for t in range(self.search_parms.search_parms["MAX_TURN"]):
            for k in node_array:
                now_pos = k.route[-1]
                if len(k.route) != 1:
                    prev_pos = k.route[-2]
                else:
                    prev_pos = -1

                for j in self.get_adjacent(now_pos):
                    if  j != prev_pos:
                        n = Node(k.route[0], k.board)
                        n.set_route(k.route[:])
                        n.board = self.swap(now_pos, j, k.board)
                        n.score, n.combo = self.calc_score(n.board)
                        n.route.append(j)
                        if len(dummy_array) > self.search_parms.search_parms["PLAYNUM"]:
                            idx = 0
                            worst = 999999
                            for d,v in enumerate(dummy_array):
                                if worst > v.score:
                                    worst = v.score
                                    idx = d
                            del dummy_array[idx]
                        dummy_array.append(n)

            node_array = []
            node_array = dummy_array[:]
            dummy_array = []

        return node_array
        # }}}

    def wrap_search_node_array(self, args): # {{{
        return args[0](*args[1:])
        # }}}

    def beam_search(self): # {{{
        # if mp.cpu_count() == 1:
        #     use_cpu_count = 1
        # else:
        #     use_cpu_count = mp.cpu_count() - 1
        # print "use cpu count: " + str(use_cpu_count)
        #
        # p = mp.Pool(use_cpu_count)
        # func_args = []
        # for i in range(self.game_parms.width * self.game_parms.height):
        #     func_args.append((self.search_node_array, i))
        # node_array = p.map(self.wrap_search_node_array, func_args)
        node_array = []
        for i in range(self.game_parms.width * self.game_parms.height):
            node_array.append(self.search_node_array(i))
        node_array = list(itertools.chain.from_iterable(node_array))  # flatten

        idx = 0
        best = 0
        for k,v in enumerate(node_array):
            if best < v.score:
                best = v.score
                idx = k

        print "best score:" + str(node_array[idx].score)
        print "best combo:" + str(node_array[idx].combo)

        return node_array[idx]
        # }}}

