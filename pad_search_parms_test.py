# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_search_parms

search_parms = pad_search_parms.SearchParms()

search_parms.show_search_parms()

print search_parms.get_search_parms_patttern()

print search_parms.search_parms["MAX_TURN"]
