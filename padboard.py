# -*- coding: utf-8 -*-

import numpy
from PIL import Image

def get_rgb(pic, box=""):
    if box == "":
        box = (0, 0, pic.width, pic.height)
    #pic.crop(box).show()
    rgbimg = pic.crop(box).convert("RGB")
    #rgb = np.array(rgbimg.getdata())
    rgb = numpy.array(rgbimg.getdata())
    return [__round(rgb[:,0]),
            __round(rgb[:,1]),
            __round(rgb[:,2])]

def color(array, flg=1):
    col = {}
    if flg == 0:
        # col["red"] = [205, 110, 130]
        # col["blue"] = [100, 140, 190]
        # col["green"] = [100, 160, 120]
        # col["light"] = [200, 175, 110]
        # col["dark"] = [165, 90, 170]
        # col["cure"] = [200, 100, 150]
        col["r"] = [205, 110, 130]
        col["b"] = [100, 140, 190]
        col["g"] = [100, 160, 120]
        col["l"] = [200, 175, 110]
        col["d"] = [165, 90, 170]
        col["c"] = [200, 100, 150]
    else:
        col["1"] = [205, 110, 130]
        col["2"] = [100, 140, 190]
        col["3"] = [100, 160, 120]
        col["4"] = [200, 175, 110]
        col["5"] = [165, 90, 170]
        col["6"] = [200, 100, 150]

    max = 0
    result = ""
    for k, c in col.items():
       tmp = numpy.corrcoef(numpy.array(array), numpy.array(c))[0][1]
       if max < tmp:
           result = k
           max = tmp
    return result

def __round(array):
    return int(round(numpy.average(array)))

#def check_board(xa, ya, xb, yb, xs, ys, path, cols, rows, flg=1):
def check_board(path, cols, rows, flg=1):
    pic = Image.open(path, 'r')
    if pic.width == 800:
        # Nexus7(2012)
        xa = 15
        ya = 560
        xb = 145
        yb = 690
        xs = 130
        ys = 130
    else:
        # SH-01F
        xa = 5
        ya = 850
        xb = 185
        yb = 1030
        xs = 180
        ys = 180

    board = ""
    for i in range(cols):
        for j in range(rows):
            box = (xa + xs*i,
                   ya + ys*j,
                   xb + xs*i,
                   yb + ys*j)
            rgb = get_rgb(pic, box)
            # print color(rgb)
            board = board + color(rgb, flg)
    return board


#path = "C:/Users/fumio/MyProject/python/pad_auto/image/pazdra_board.png"
#check_board(xa, ya, xb, yb, xs, ys, path, 6, 5)

#if __name__ == "__main__":
#    '''
#        xa : 始点, xs : Blockの幅, xb : 終点
#　　　　 ya : 始点, ys : Blockの高さ, yb : 終点
#    '''
#    xa = 40
#    ya = 400
#    xb = 95
#    yb = 455
#    xs = 65
#    ys = 65
#    #pic = Image.open("/path/to/Image.png", 'r')
#    pic = Image.open("C:/Users/fumio/MyProject/python/pad_auto/image/pazdra_board.png", 'r')
#    #print "pic width: " + str(pic.width) + ", pic height: " + str(pic.height)
#    for i in xrange(6):
#        for j in xrange(5):
#           box = (xa + xs*i,
#                  ya + ys*j,
#                  xb + xs*i,
#                  yb + ys*j)
#           rgb = get_rgb(pic, box)
#           print color(rgb)
#           #print rgb
