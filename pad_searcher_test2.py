# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_searcher

board = """
ddcccd
cddddd
dddddd
dccddc
cddddd
""".replace('\n', '')

print pad_searcher.search_with_beam(board)
