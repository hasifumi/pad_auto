# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_route

cols = 6
rows = 5
pic_width = 1080

route = [0,1,2,3,4,5,6,7]

pad_route = pad_route.Route(cols, rows, pic_width)

print "is_nexus: " + str(pad_route.is_nexus)
print pad_route.get_route(route)
