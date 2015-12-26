# -*- coding: utf-8 -*-

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
        '1line-green': 1.0,
        '1line-light': 0.0,
        '1line-dark' : 0.0,
        '1line-cure' : 0.0,
        }# }}}

PARMS = DEFAULT_PARMS

def show_parms(PARMS):# {{{
    print "show current parms ..."
    details = [
        'name',
        'red',
        'blue',
        'green',
        'light',
        'dark',
        'cure',
        '3colors',
        '4colors',
        '5colors',
        '3colors+cure',
        '4colors+cure',
        '5colors+cure',
        '4drops-red',
        '4drops-blue',
        '4drops-green',
        '4drops-light',
        '4drops-dark',
        '4drops-cure',
        '5drops-red',
        '5drops-blue',
        '5drops-green',
        '5drops-light',
        '5drops-dark',
        '5drops-cure',
        '1line-red',
        '1line-blue',
        '1line-green',
        '1line-light',
        '1line-dark',
        '1line-cure',
        ]

    for k in details:
        if PARMS.has_key(k):
            if isinstance(PARMS[k], float) and PARMS[k] != 0.0:
                print " " + str(k) + ": " + str(PARMS[k])
            elif isinstance(PARMS[k], str):
                print " " + str(k) + ": " + str(PARMS[k])

show_parms(DEFAULT_PARMS)

