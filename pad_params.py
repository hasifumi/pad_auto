# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

class GameParams:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def output(self):
        print("WIDTH :"+str(self.width))
        print("HEIGHT:"+str(self.height))


if __name__ == '__main__':
    p = GameParams(6, 5)
    p.output()
