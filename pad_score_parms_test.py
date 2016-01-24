
# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pad_score_parms

score_parms = pad_score_parms.ScoreParms()
score_parms.set_score_parms("awaken lucifer")
print score_parms.score_parms

score_parms.show_score_parms()
print ""

print score_parms.get_score_parms_patttern()
