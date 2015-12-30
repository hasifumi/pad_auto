# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

def wrap_myfunc(args):
    return args[0](*args[1:])

def myfunc(a, b, c, d):
    ans = (a + b) * (c + d)
    print " myfunc answer: " + str(ans) + ", a: " + str(a) + ", b:" + str(b) + ", c:" + str(c) + ", d:" + str(d)
    return ans

if __name__ == '__main__':
    from multiprocessing import Pool
    p = Pool()
    func_args = []
    for a in [1, 2, 3, 4, 5]:
        for b in xrange(2):
            func_args.append( (myfunc, a, b, a+1, b+1) )
    results = p.map(wrap_myfunc, func_args)
    print results
