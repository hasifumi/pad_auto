# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

def xy2idx(x, y, width):# {{{
    return y*width+x# }}}

def make_adjcent(width, height):# {{{
    # print "width: " + str(width) + ", height: " + str(height)
    # print ""
    i = 0
    ary = []
    for h in range(height):
        for w in range(width):
            ary_b = []
            # print "w: " + str(w) + ", (w-1): " + str(w-1) + ", (w+1): " + str(w+1)
            # print "h: " + str(h) + ", (h-1): " + str(h-1) + ", (h+1): " + str(h+1)
            if 0 <= w - 1:
                ary_b.append(xy2idx(w - 1, h, width))
                # print "(w-1): " + str(w-1) + ", h: " + str(h)
                # print "append1 : " + str(xy2idx(w - 1, h, width))
            if w + 1 < width:
                ary_b.append(xy2idx(w + 1, h, width))
                # print "(w+1): " + str(w+1) + ", h: " + str(h)
                # print "append2 : " + str(xy2idx(w + 1, h, width))
            if 0 <= h - 1:
                ary_b.append(xy2idx(w, h - 1, width))
                # print "w: " + str(w) + ", (h-1): " + str(h-1)
                # print "append3 : " + str(xy2idx(w , h - 1, width))
            if h + 1 < height:
                ary_b.append(xy2idx(w, h + 1, width))
            #     print "w: " + str(w) + ", (h+1): " + str(h+1)
            #     print "append4 : " + str(xy2idx(w , h + 1, width))
            # print "ary_b: " + str(ary_b)
            ary.append(ary_b)
            # print "ary: " + str(ary)
            # print ""
    return ary# }}}

def make_renketsu(width, height, vector):
    # print "width: " + str(width) + ", height: " + str(height) + ", vector: " + str(vector)
    # print ""
    i = 0
    ary = []
    for h in range(height):
        for w in range(width):
            if vector == "h":  # horizon
                # print "w: " + str(w) + ", (w+1): " + str(w+1) + ", (w+2): " + str(w+2)
                if   w+1 < width and w+2 < width:
                    ary.append([xy2idx(w, h, width), xy2idx(w+1, h, width), xy2idx(w+2, h, width)])
                else:
                    ary.append([])
            elif vector == "v":  # vertical
                # print "h: " + str(h) + ", (h+1): " + str(h+1) + ", (h+2): " + str(h+2)
                if   h+1 < height and h+2 < height:
                    ary.append([xy2idx(w, h, height), xy2idx(w+1, h, height), xy2idx(w+2, h, height)])
                else:
                    ary.append([])
            # print "ary_b: " + str(ary_b)
            # print "ary: " + str(ary)
            # print ""
    return ary

if __name__ == "__main__":
    # ary = make_adjcent(5, 4)
    ary = make_renketsu(5, 4, "h")
    print ary

#    renketsu_5x4_h = [# {{{
#            [0, 1, 2],
#            [1, 2, 3],
#            [2, 3, 4],
#            [],
#            [],
#            [5, 6, 7],
#            [6, 7, 8],
#            [7, 8, 9],
#            [],
#            [],
#            [10, 11, 12],
#            [11, 12, 13],
#            [12, 13, 14],
#            [],
#            [],
#            [15, 16, 17],
#            [16, 17, 18],
#            [17, 18, 19],
#            [],
#            [],
#    ]# }}}

#    adjacent_5x4 = [# {{{
#            [1, 5],             # 0
#            [0, 2, 6],
#            [1, 3, 7],
#            [2, 4, 8],
#            [3, 9],
#            [0, 6, 10],
#            [1, 5, 7, 11],
#            [2, 6, 8, 12],
#            [3, 7, 9, 13],
#            [4, 8, 14],
#            [5, 11, 15],
#            [6, 10, 12, 16],
#            [7, 11, 13, 17],
#            [8, 12, 14, 18],
#            [9, 13, 19],
#            [10, 16],
#            [11, 15, 17],
#            [12, 16, 18],
#            [13, 17, 19],
#            [14, 18]
#    ]# }}}

