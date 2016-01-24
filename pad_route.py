# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class Route():

    def __init__(self, cols, rows, pic_width):# {{{
        self.cols = cols
        self.rows = rows
        self.pic_width = pic_width
        self.is_nexus = self.chk_nexus()
        # }}}

    def chk_nexus(self):# {{{
        if self.pic_width == 800:
            return True
        else:
            return False
        # }}}

    def idx2xy(self, idx):# {{{
        return[int(idx/self.cols), int(idx%self.cols)]
        # }}}

    def conv_x(self, i):# {{{
        if self.is_nexus:
            if   self.cols == 5:
                return 15 + 78 + 155 * (int(i))
            elif self.cols == 6:
                return 15 + 65 + 130 * (int(i))
        else:
            if   self.cols == 5:
                return 5  + 105 + 210 * (int(i))
            elif self.cols == 6:
                return 5  +  90 + 180 * (int(i))
            elif self.cols == 7:
                return 25 +  73 + 145 * (int(i))
        # }}}

    def conv_y(self, i):# {{{
        if self.is_nexus:
            if self.cols == 5:
                return 575 + 78 + 155 * (int(i))
            elif self.cols == 6:
                return 560 + 65 + 130 * (int(i))
        else:
            if self.cols == 5:
                return 865 + 105 + 210 * (int(i))
            elif self.cols == 6:
                return 860 +  90 + 180 * (int(i))
            elif self.cols == 7:
                return 850 +  73 + 145 * (int(i))
        # }}}

    def calc_i(self, flag, ary):# {{{
        pos_i = "\""
        for i,v in enumerate(ary):
            if flag == "x":
                pos_i += str(self.conv_x(ary[i]))
            else:
                pos_i += str(self.conv_y(ary[i]))
            pos_i += ","
        pos_i = pos_i.rstrip(",")
        pos_i += "\""
        return pos_i# }}}

    def get_route(self, route):# {{{
        x = []
        y = []
        for r in route:
            ans = self.idx2xy(r)
            x.append(ans[1])
            y.append(ans[0])
        pos_x = self.calc_i("x", x)
        pos_y = self.calc_i("y", y)
        return (pos_x, pos_y)
        # }}}

