module "pad_combo", package.seeall

class PadCombo
	new: (@cols, @rows, @board, @pad_score_parms) =>

	str2lst:(lst) =>-- {{{
		ret = [ [0 for col = 1, @cols] for row = 1, @rows]
		if len(@board) == @cols * @rows
			i = 0
			for row = 1, @rows
				for col = 1, @cols
					ret[row][col] = @board[i]
					i += 1
			return ret
		-- }}}

    xy2idx: (x, y) =>-- {{{
		return (y - 1) * @cols + x
	-- }}}

	idx2xy: (idx) =>-- {{{
		x = idx % @cols
		if x == 0
		    x = @cols
		    y = idx / @cols
		    print "idx:", idx
		    print "@cols:", @cols
		    print "1"
		else
		    y = (idx - x) / @cols + 1
		    print "idx:", idx
		    print "@cols:", @cols
		    print "2"
		return x, y
	-- }}}

    make_adjacent: =>-- {{{
		ary = {}
		for row = 1, @rows
			for col = 1, @cols
				ary_b = {}
				print "row:", row, ", col:", col
				if 1 <= col - 1
					table.insert(ary_b, @xy2idx(col - 1, row))
					print "1) col - 1:", (col - 1), ", row:", row,", xy2idx:", @xy2idx(col - 1, row)
				if col + 1 <= @cols
					table.insert(ary_b, @xy2idx(col + 1, row))
					print "2) col + 1:", (col + 1), ", row:", row,", xy2idx:", @xy2idx(col + 1, row)
				if 1 <= row - 1
					table.insert(ary_b, @xy2idx(col, row - 1))
					print "3) col:", col, ", (row - 1):", (row - 1),", xy2idx:", @xy2idx(col, row - 1)
				if row + 1 <= @rows
					table.insert(ary_b, @xy2idx(col, row + 1))
					print "4) col:", col, ", (row + 1):", (row + 1),", xy2idx:", @xy2idx(col, row + 1)
				-- print "col - 1:",(col - 1)
				-- print "col + 1:",(col + 1)
				-- print "row - 1:",(row - 1)
				-- print "row + 1:",(row + 1)
				print unpack ary_b
				table.insert(ary, ary_b)
		return ary
	-- }}}

	aaa

-- p_cmb = PadCombo 5, 4, "rrrrrbbbbbgggggccccc"
p_cmb = PadCombo 3, 2, "rrrbbb"
print "@cols:", p_cmb.cols
print "@board:", p_cmb.board
print "@xy2idx:", p_cmb\xy2idx 2, 1
x, y = p_cmb\idx2xy 5
print "x:", x
print "y:", y
print "@idx2xy:", x, y
-- print ""
-- print p_cmb\make_adjacent!

--
-- class PadCombo():
--
--     def __init__(self, cols, rows, board, pad_score_parms):# {{{
--         self.cols = cols
--         self.rows = rows
--         self.board = board
--         self.board_l = self.str2lst(self.board)
--         self.erase_l = copy.deepcopy(self.board_l)
--         self.erase2_l = copy.deepcopy(self.board_l)
--         self.fall_l = copy.deepcopy(self.board_l)
--         self.combo = {}
--         self.combo_count = 0
--         self.combo_seq = {}
--         self.combo_color = {}
--         self.combo_color_count = {}  # cure以外の属性（色）カウンタ（例：3色）
--         self.combo_cure_count = {}
--         self.score = 0
--         self.adjacent = self.make_adjacent()
--         self.renketsu_h = self.make_renketsu("h")
--         self.renketsu_v = self.make_renketsu("v")
--         # }}}
--
--     # 文字列を2二元配列に格納
--     def str2lst(self, board):# {{{
--         ret = [[0 for col in range(self.cols)] for row in range(self.rows)]
--         if len(board) == self.cols * self.rows:
--             i = 0
--             for row in range(self.rows):
--                 for col in range(self.cols):
--                     ret[row][col] = board[i]
--                     i += 1
--         return ret
--         # }}}
--
--     # ユーティリティ関数
--     def xy2idx(self, x, y):# {{{
--         return y * self.cols + x
--         # }}}
--
--     def idx2xy(self, idx):# {{{
--         return[int(idx / self.cols), int(idx % self.cols)]
--         # }}}
--
--     def make_adjacent(self):# {{{
--         ary = []
--         for row in range(self.rows):
--             for col in range(self.cols):
--                 ary_b = []
--                 if 0 <= col - 1:
--                     ary_b.append(self.xy2idx(col - 1, row))
--                 if col + 1 < self.cols:
--                     ary_b.append(self.xy2idx(col + 1, row))
--                 if 0 <= row - 1:
--                     ary_b.append(self.xy2idx(col, row - 1))
--                 if row + 1 < self.rows:
--                     ary_b.append(self.xy2idx(col, row + 1))
--                 ary.append(ary_b)
--         return ary# }}}
--
--     def make_renketsu(self, vector):# {{{
--         ary = []
--         for row in range(self.rows):
--             for col in range(self.cols):
--                 if vector == "h":  # horizon
--                     if   col+2 < self.cols:
--                         ary.append([self.xy2idx(col, row), self.xy2idx(col+1, row), self.xy2idx(col+2, row)])
--                     else:
--                         ary.append([])
--                 elif vector == "v":  # vertical
--                     if   row+2 < self.rows:
--                         ary.append([self.xy2idx(col, row), self.xy2idx(col, row+1), self.xy2idx(col, row+2)])
--                     else:
--                         ary.append([])
--         return ary# }}}
--
--     def check_erasable(self):# {{{
--         ers = 0
--         # 横方向の消去可能性チェック
--         for j in range(self.rows):
--             for i in range(self.cols - 2):
--                 if self.isRenketsu(i, j, "h") == True:
--                     self.erase_l[j][i] = self.str_e(ers)
--                     self.erase_l[j][i+1] = self.str_e(ers)
--                     self.erase_l[j][i+2] = self.str_e(ers)
--                     self.combo[ers] = {
--                             'start_x_pos': i,
--                             'start_y_pos': j,
--                             'vector': "h",
--                             'color': self.board_l[j][i],
--                             'combo_seq': ers,
--                             }
--                     # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
--                     ers += 1
--         # 縦方向の消去可能性チェック
--         for j in range(self.rows - 2):
--             for i in range(self.cols):
--                 if self.isRenketsu(i, j, "v") == True:
--                     self.erase_l[j][i] = self.str_e(ers)
--                     self.erase_l[j+1][i] = self.str_e(ers)
--                     self.erase_l[j+2][i] = self.str_e(ers)
--                     self.combo[ers] = {
--                             'start_x_pos': i,
--                             'start_y_pos': j,
--                             'vector': "v",
--                             'color': self.board_l[j][i],
--                             'combo_seq': ers,
--                             }
--                     # combo : 0)find_seq, 1)start_x_pos, 2)start_y_pos, 3)vector(h/v), 4)color, 5)combo_seq
--                     ers += 1
--         # }}}
--
--     def check_renkentsu_erasable(self):# {{{
--         cmb_l = list(self.board)
--         cnt = 0
--         for k, v in self.combo.iteritems():
--             if v['vector'] == "h":
--                 for j in self.renketsu_h[self.xy2idx(v['start_x_pos'], v['start_y_pos'])]:
--                     cmb_l[j] = self.str_e(v['combo_seq'])
--             elif v['vector'] == "v":
--                 for j in self.renketsu_v[self.xy2idx(v['start_x_pos'], v['start_y_pos'])]:
--                     cmb_l[j] = self.str_e(v['combo_seq'])
--         self.erase2_l = cmb_l# }}}
--
--     def isRenketsu(self, x, y, vector="h"):# {{{
--         if vector == "h":  # 横方向
--             if self.board_l[y][x] == self.board_l[y][x+1] == self.board_l[y][x+2]:
--                 return True
--             else:
--                 return False
--         elif vector == "v":  # 縦方向
--             if self.board_l[y][x] == self.board_l[y+1][x] == self.board_l[y+2][x]:
--                 return True
--             else:
--                 return False
--         else:
--             return False
--         # }}}
--
--     # グループ1の各ドロップの近接リストにグループ2の各ドロップが存在するかを調査する関数
--     def isKinsetsu(self, x1, y1, v1, x2, y2, v2):  # x:x座標、y:y座標, v:方向# {{{
--         idx1 = self.xy2idx(x1, y1)
--         idx2 = self.xy2idx(x2, y2)
--         if v1 == "h":
--             for i in self.renketsu_h[idx1]:
--                 for j in self.adjacent[i]:
--                     if v2 == "h":
--                         for k in self.renketsu_h[idx2]:
--                             if j == k:
--                                 return True
--                     elif v2 == "v":
--                         for k in self.renketsu_v[idx2]:
--                             if j == k:
--                                 return True
--         elif v1 == "v":
--             for i in self.renketsu_v[idx1]:
--                 for j in self.adjacent[i]:
--                     if v2 == "h":
--                         for k in self.renketsu_h[idx2]:
--                             if j == k:
--                                 return True
--                     elif v2 == "v":
--                         for k in self.renketsu_v[idx2]:
--                             if j == k:
--                                 return True
--         return False
--         # }}}
--
--     def str_e(self,e):# {{{
--         if 0 <= e <= 9:
--             return str(e)
--         elif e == 10:
--             return "A"
--         elif e == 11:
--             return "B"
--         elif e == 12:
--             return "C"
--         elif e == 13:
--             return "D"
--         elif e == 14:
--             return "E"
--         elif e == 15:
--             return "F"
--         elif e == 16:
--             return "G"
--         elif e == 17:
--             return "H"
--         elif e == 18:
--             return "I"
--         elif e == 19:
--             return "J"
--         elif e == 20:
--             return "K"
--         elif e > 20:
--             return "Z"# }}}
--
--     def print_lst2str(self, mod="board"):# {{{
--         if mod == "board":
--             lst = copy.deepcopy(self.board_l)
--         elif mod == "erase":
--             lst = copy.deepcopy(self.erase_l)
--         elif mod == "erase2":
--             lst = copy.deepcopy(self.erase2_l)
--
--         strs = "".join(list(itertools.chain.from_iterable(lst)))
--         for row in range(self.rows):
--             print strs[ row * self.cols : row * self.cols + self.cols ]
--         # }}}
--
--     def calc_combo(self):# {{{
--         cmb = -1
--         cmb_keys = {}
--         cmb_seq = {}
--         cmb_color = {}
--         cmb_color_count = 0  # cure以外の属性（色）カウンタ　（例：3色）
--         cmb_cure_count = 0
--         for k, v in self.combo.iteritems():
--             if k in cmb_keys:
--                 cmb_keys[k] += 1
--             else:
--                 cmb_keys[k] = 1
--             if cmb < v['combo_seq']:
--                 cmb += 1
--                 cmb_seq[cmb] = {
--                         'first_find_seq': k,
--                         'color': v['color'],
--                         'vector': v['vector'],
--                         'count': 1,
--                         }
--                 if v['color'] in cmb_color:
--                     cmb_color[v['color']] += 1
--                 else:
--                     cmb_color[v['color']] = 1
--                     if v['color'] == 'c':
--                         cmb_cure_count += 1
--                     else:
--                         cmb_color_count += 1
--             for k2, v2 in self.combo.iteritems():
--                 if k2 in cmb_keys:
--                     pass
--                 else:
--                     if v['color'] == v2['color']:   # 同色か？
--                         # vの各ドロップの近接リストにcmb2の各ドロップがいるか？
--                         if self.isKinsetsu(v['start_x_pos'], v['start_y_pos'], v['vector'], v2['start_x_pos'], v2['start_y_pos'], v2['vector']):
--                             v['combo_seq'] = cmb
--                             v2['combo_seq'] = cmb
--                             cmb_seq[cmb]['count'] += 1
--         self.combo_count = cmb + 1
--         self.combo_seq = cmb_seq
--         self.combo_color = cmb_color
--         self.combo_color_count = cmb_color_count
--         self.combo_cure_count = cmb_cure_count
--         return
--         # }}}
--
--     def calc_score(self, pad_score_parms):# {{{
--         score = 0
--         PARMS = pad_score_parms.score_parms
--
--         # コンボ優先
--         score += self.combo_count * 100
--
--         # 属性優先（色優先）
--         for k, v in self.combo_color.iteritems():# {{{
--             if   k == "r":
--                 if PARMS.has_key('red'):
--                     score += PARMS['red'] * 100
--             elif k == "b":
--                 if PARMS.has_key('blue'):
--                     score += PARMS['blue'] * 100
--             elif k == "g":
--                 if PARMS.has_key('green'):
--                     score += PARMS['green'] * 100
--             elif k == "l":
--                 if PARMS.has_key('light'):
--                     score += PARMS['light'] * 100
--             elif k == "d":
--                 if PARMS.has_key('dark'):
--                     score += PARMS['dark'] * 100
--             elif k == "c":
--                 if PARMS.has_key('cure'):
--                     score += PARMS['cure'] * 100# }}}
--
--         # 多色
--         if self.combo_color_count >= 3 and PARMS.has_key('3colors'): # {{{
--             score += PARMS['3colors'] * 1000
--         if self.combo_color_count >= 3 and self.combo_cure_count >= 1 and PARMS.has_key('3colors+cure'):
--             score += PARMS['3colors+cure'] * 1000
--         if self.combo_color_count >= 4 and PARMS.has_key('4colors'):
--             score += PARMS['4colors'] * 1000
--         if self.combo_color_count >= 4 and self.combo_cure_count >= 1 and PARMS.has_key('4colors+cure'):
--             score += PARMS['4colors+cure'] * 1000
--         if self.combo_color_count >= 5 and PARMS.has_key('5colors'):
--             score += PARMS['5colors'] * 1000
--         if self.combo_color_count >= 5 and self.combo_cure_count >= 1 and PARMS.has_key('5colors+cure'):
--             score += PARMS['5colors+cure'] * 1000# }}}
--
--         # 列優先
--         color = self.chk_1LineColor()# {{{
--         for k, v in color.iteritems():
--             if   v == 'r' and PARMS.has_key('1line-red'):
--                 score += PARMS['1line-red']  * 10000
--             elif v == 'b' and PARMS.has_key('1line-blue'):
--                 score += PARMS['1line-blue'] * 10000
--             elif v == 'g' and PARMS.has_key('1line-green'):
--                 score += PARMS['1line-green'] * 10000
--             elif v == 'l' and PARMS.has_key('1line-light'):
--                 score += PARMS['1line-light'] * 10000
--             elif v == 'd' and PARMS.has_key('1line-dark'):
--                 score += PARMS['1line-dark'] * 10000
--             elif v == 'c' and PARMS.has_key('1line-cure'):
--                 score += PARMS['1line-cure'] * 10000# }}}
--
--         # 4つ消し、5つ消し
--         drops4 = self.chk_drops4()
--         drops5 = self.chk_drops5()
--
--         for k, v in drops4.iteritems(): # {{{
--             if   k == 'r' and PARMS.has_key('4drops-red'):
--                 score += PARMS['4drops-red'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-red'] * 5000 * -1     # 罰
--             elif k == 'b' and PARMS.has_key('4drops-blue'):
--                 score += PARMS['4drops-blue'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-blue'] * 5000 * -1    # 罰
--             elif k == 'g' and PARMS.has_key('4drops-green'):
--                 score += PARMS['4drops-green'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-green'] * 5000 * -1    # 罰
--             elif k == 'l' and PARMS.has_key('4drops-light'):
--                 score += PARMS['4drops-light'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-light'] * 5000 * -1    # 罰
--             elif k == 'd' and PARMS.has_key('4drops-dark'):
--                 score += PARMS['4drops-dark'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-dark'] * 5000 * -1    # 罰
--             elif k == 'c' and PARMS.has_key('4drops-cure'):
--                 score += PARMS['4drops-cure'] * 5000
--                 if drops5.has_key(k):
--                     score += PARMS['4drops-cure'] * 5000 * -1    # 罰
--         return (score, self.combo_count)# }}}
--
--         for k, v in drops5.iteritems():# {{{
--             if   k == 'r' and PARMS.has_key('5drops-red'):
--                 score += PARMS['5drops-red'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-red'] * 5000 * -1     # 罰
--             elif k == 'b' and PARMS.has_key('5drops-blue'):
--                 score += PARMS['5drops-blue'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-blue'] * 5000 * -1    # 罰
--             elif k == 'g' and PARMS.has_key('5drops-green'):
--                 score += PARMS['5drops-green'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-green'] * 5000 * -1    # 罰
--             elif k == 'l' and PARMS.has_key('5drops-light'):
--                 score += PARMS['5drops-light'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-light'] * 5000 * -1    # 罰
--             elif k == 'd' and PARMS.has_key('5drops-dark'):
--                 score += PARMS['5drops-dark'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-dark'] * 5000 * -1    # 罰
--             elif k == 'c' and PARMS.has_key('5drops-cure'):
--                 score += PARMS['5drops-cure'] * 5000
--                 if drops4.has_key(k):
--                     score += PARMS['5drops-cure'] * 5000 * -1    # 罰# }}}
--
--         self.score = score
--
--         return (self.score, self.combo_count)# }}}
--
--     def chk_1LineColor(self):# {{{
--         color = {}
--         for y in range(self.rows):
--             for x in range(self.cols):
--                 if color.has_key(y):
--                     if color[y] != self.board[self.xy2idx(x, y)]:
--                         color[y] = ""
--                         break
--                 else:
--                     color[y] = self.board[self.xy2idx(x, y)]
--         return  color# }}}
--
--     def chk_drops4(self):# {{{
--         drops4 = {}
--         for k, v in self.combo_seq.iteritems():
--             if v['count'] == 2:
--                 if v['color'] in drops4:
--                     drops4[v['color']] += 1
--                 else:
--                     drops4[v['color']] = 1
--         return drops4# }}}
--
--     def chk_drops5(self):# {{{
--         drops5 = {}
--         for k, v in self.combo_seq.iteritems():
--             if v['count'] == 4:   # why "count:4" is drop5?
--                 if v['color'] in drops5:
--                     drops5[v['color']] += 1
--                 else:
--                     drops5[v['color']] = 1
--         return drops5# }}}
--
--     def chk_drops_color(self):# {{{
--         drops_color = {}
--         for d in self.board:
--             if d in drops_color:
--                 drops_color[d] += 1
--             else:
--                 drops_color[d] = 1
--         return drops_color# }}}
--
