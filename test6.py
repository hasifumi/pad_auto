# -*- coding: utf-8 -*-
# vim: foldmethod=marker  :

from PIL import Image

path = ".\screen.png"

pic = Image.open(path, 'r')

print dir(pic)

print pic.size

key1 = str(pic.size[0])

print key1
