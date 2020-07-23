# -*- coding: utf-8 -*-

import win32gui
import time

a = win32gui.FindWindow(None, "SC-03L")
print(win32gui.GetWindowText(a))
if a is not 0:
    win32gui.SetForegroundWindow(a)

# a = win32gui.GetForegroundWindow()
# a_text = win32gui.GetWindowText(a)
# print(a_text)
# print("wait 5 second.. ")
#
# time.sleep(5)
#
# b = win32gui.GetForegroundWindow()
# b_text = win32gui.GetWindowText(a)
# print(b_text)
# print("change current window...")
#
# time.sleep(5)
#
# win32gui.SetForegroundWindow(a)
# print("change current window, again...")
#
# time.sleep(5)
#
# win32gui.SetForegroundWindow(b)
