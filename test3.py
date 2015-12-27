# -*- coding: utf-8 -*-

DEFAULT_GAME_PARMS = {
        'max_turn' : 40,
        'PLAYNUM' : 500,
        'SWIPE' : 4,
        }

GAME_PARMS_PATTERN = {
        'default' : {
            'MAX_TURN' : 40,
            'PLAYNUM'  : 500,
            'SWIPE'    : 4,
            },
        'win_tablet' : {
            'MAX_TURN' : 30,
            'PLAYNUM'  : 400,
            'SWIPE'    : 5,
            },
        }

def print_game_parms():
    print "show game parms ... "
    print " MAX_TURN : " + str(MAX_TURN)
    print " PLAYNUM  : " + str(PLAYNUM)
    print " SWIPE    : " + str(SWIPE)

def set_game_parms(pattern):
    if GAME_PARMS_PATTERN.has_key(pattern):
        if GAME_PARMS_PATTERN[pattern].has_key('MAX_TURN') and GAME_PARMS_PATTERN[pattern].has_key('PLAYNUM') and GAME_PARMS_PATTERN[pattern].has_key('SWIPE'):
            print "set game parms ... "
            print " name     : " + str(pattern)
            print " MAX_TURN : " + str(GAME_PARMS_PATTERN[pattern]['MAX_TURN'])
            print " PLAYNUM  : " + str(GAME_PARMS_PATTERN[pattern]['PLAYNUM'])
            print " SWIPE    : " + str(GAME_PARMS_PATTERN[pattern]['SWIPE'])
            return (GAME_PARMS_PATTERN[pattern]['MAX_TURN'], GAME_PARMS_PATTERN[pattern]['PLAYNUM'], GAME_PARMS_PATTERN[pattern]['SWIPE'])
    else:
        return (40, 500, 5)

MAX_TURN, PLAYNUM, SWIPE = set_game_parms('default')
print_game_parms()
MAX_TURN, PLAYNUM, SWIPE = set_game_parms('win_tablet')

