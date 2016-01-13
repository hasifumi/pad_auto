# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

#import padboard
import padboard2
import pazdracombo
import time
import sys

argvs = sys.argv
argc = len(argvs)

#print argvs
for i in range(len(argvs)):
    print "argvs[" + str(i) + "]: " + str(argvs[i])
print argc
print

if (argc != 4):
    print "Usage: # python %s path width height" % argvs[0]
    quit()

start_time = time.time()

#path = ".\screen_sh-01f_5x4.png"
#WIDTH = 5
#HEIGHT = 4
#answer_5x4 = "dbdcbbddcrldrgllrcbc"

#board = pazdracombo.convert_h_w_5x4(padboard.check_board(path, WIDTH, HEIGHT, 0))
temp_board, width = padboard2.check_board(argvs[1], int(argvs[2]), int(argvs[3]), 0)
board = pazdracombo.convert_h_w_5x4(temp_board)
print "[5x4]"
print board
print width

