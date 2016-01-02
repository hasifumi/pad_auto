# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import multiprocessing as mp

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print " I'm " + str(self.name) + ", " + str(self.age) + "years old."

    def getName(self):
        return self.name

def wrap_func(args):
    return args[0](*args[1:])

def plus_years(person, years, last_name):
    person.age = person.age + years
    person.name = person.name + last_name
    return person

def testMP(persons):

    per1 = []
    per2 = []
    years = 5
    last_name = " hashidume"

    for p in persons:
        per = Person(p['name'], p['age'])
        per.introduce()
        per1.append(per)

    print type(per1)
    print per1

    print "cpu count: " + str(mp.cpu_count())

    #for p in per1:
    #    per2.append(plus_years(p, years))

    pl = mp.Pool()
    func_args = []
    for p in per1:
        func_args.append((plus_years, p, years, last_name))
    results = pl.map(wrap_func, func_args)
    print results

    for r in results:
        r.introduce()

    #print per2

    #for p in per2:
    #    p.introduce()

if __name__ == '__main__':
    persons = [
            {'name': "Fumio",   'age':43},
            {'name': "Yuriko",  'age':44},
            {'name': "Rio",     'age':11},
            {'name': "Natsuki", 'age':6},
            ]

    testMP(persons)


#    p = multiprocessing.Pool()
#    func_args = []
#    #for na in node_array:
#    for na in iter(node_array):
#        #print "na: " + str(na)
#        func_args.append((search_node_array, width, height, max_turn, playnum, parms, na, dummy_array))
#        #func_args = itrs.izip(itrs.repeat('search_node_array'), itrs.repeat('width'), itrs.repeat('height'), itrs.repeat('max_turn'), itrs.repeat('playnum'), itrs.repeat('parms'), itrs.repeat('na'), itrs.repeat('dummy_array'))
#    #print "func_args: " + str(func_args)
#    results = p.map(wrap_search_node_array, func_args)
#    print "results :" + str(results)
