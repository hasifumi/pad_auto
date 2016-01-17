# -*- coding: utf-8 -*-

import subprocess

png_file_name = "screen.png"
WIDTH = "6"
HEIGHT = "5"

#cmd = "python padboard.py "+ png_file_name + " 5 4"
#print cmd
#p = subprocess.Popen(cmd.strip().split(" "), stdout=subprocess.PIPE)

cmd = ["python", "padboard2.py", png_file_name, WIDTH, HEIGHT]
p = subprocess.check_output(cmd)
print p

