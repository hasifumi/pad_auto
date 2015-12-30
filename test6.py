# -*- coding: utf-8 -*-

from multiprocessing import Pool, cpu_count
import time

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(an):
    a, n = an
    t = 0
    for b in range(a, n+1):
        for c in range(b, n+1):
            t += gcd(gcd(a,b), c)
    return t

if __name__ == '__main__':
    n = 300

    print('cpu : %d' % 1)
    st = time.time()
    ans = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                ans += gcd(gcd(a, b), c)
    print('answer : %d' % ans)
    print('time : %.3f s' % (time.time()-st))


    print('\ncpu : %d' % cpu_count())
    st = time.time()
    p = Pool()
    ans = sum(p.map(f, [(a,n) for a in range(1, n+1)]))
    print('answer : %d' % ans)
    print('time : %.3f s' % (time.time()-st))
