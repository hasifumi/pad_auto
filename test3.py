
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

PARMS_PATTERN = {
        'saria, tall': {
            'red': 5.0,
            'light': 10.0,
            'cure': 5.0,
            '4drops-red' : 5.0,
            '4drops-light' : 10.0,
            '1line-red': 10.0,
            '1line-light': 50.0,
            },
        'blue-sonia, ryune': {
            'blue': 10.0,
            'dark': 5.0,
            'cure': 5.0,
            '5drops-blue': 50.0,
            '1line-blue': 50.0,
            '1line-dark': 10.0,
            }
        }

PARMS = DEFAULT_PARMS

def select_parms_pattern(PARMS):# {{{
    print "current pattern name = " + PARMS['name']
    cnt = 0
    patterns = {}
    patterns_str = ""
    for k in PARMS_PATTERN.keys():
        patterns[cnt] = k
        patterns_str = patterns_str + str(cnt + 1) + ": " + k + ", "
        cnt += 1
    print "select parms pattern (" + patterns_str + ")"
    input_test_word = input(">>>  ")
    input_test_word -= 1
    if PARMS_PATTERN.has_key(patterns[input_test_word]):
        PARMS['name'] = patterns[input_test_word]
        for k in PARMS_PATTERN[patterns[input_test_word]].keys():
            if PARMS.has_key(k):
                PARMS[k] = PARMS_PATTERN[patterns[input_test_word]][k]
    return PARMS# }}}

PARMS = select_parms_pattern(PARMS)

print "name = " + PARMS['name']
print PARMS
