# -*- coding: utf-8 -*-

import cv2

src = cv2.imread("./image/pazdra_board.png", 1)
#tmp = cv2.imread("./image/red_drop.png", 1)
#col = ['red', 'blue', 'green', 'light', 'dark', 'cure']
col = ['red']
tmp = []
for c in col:
    tmp.append([cv2.imread("./image/" + c + "_drop2.png", 1), c])
#tmp = cv2.imread("./image/blue_drop.png", 1)
output = {}

for t in tmp:
    for i in range(30):
        res = cv2.matchTemplate(src, t[0], cv2.TM_CCOEFF_NORMED)
        (minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)

        #print "({0}, {1}) score = {2}\n".format(maxloc[0], maxloc[1], maxval)

        (h, w, d) = t[0].shape

        rect_1 = (maxloc[0], maxloc[1])
        rect_2 = (maxloc[0] + w, maxloc[1] + h)
        #print "size ({0}, {1})\n".format(w, h)
        cv2.rectangle(src, rect_1, rect_2, 0x00ff00)
        if (str(maxloc[0]) + str(maxloc[1])) in output:
            continue
        else:
            output[str(maxloc[0]) + str(maxloc[1])] = [maxloc[0], maxloc[1], w, h, t[1]]  # キー：開始点のx＋y, 開始点x, 開始点y, 幅, 高さ, 色

cv2.imwrite("./image/py-output.png", src)
print output
