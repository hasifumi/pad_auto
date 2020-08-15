# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

# import pyautogui
import win32gui
import time
# import PIL
from PIL import ImageGrab
import os
import win32api

def set_activeWindow(window_id):# {{{

    VK_TAB = 0x09
    VK_SHIFT = 0x10
    VK_MENU = 0x12
    KEYEVENTF_KEYUP = 0x2
    start = time.time()

    while True:
        hw = win32gui.GetForegroundWindow()
        print(hw)
        if window_id == hw:
            break
        time.sleep(0.5)
        if time.time() - start > 5:
            print("fail set_activeWindow()!")
            break

        win32api.keybd_event(VK_MENU, 0, 0)
        win32api.keybd_event(VK_SHIFT, 0, 0)
        win32api.keybd_event(VK_TAB, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(VK_TAB, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP)
        time.sleep(0.1)# }}}


a = win32gui.FindWindow(None, "SC-03L")
print(win32gui.GetWindowText(a))
if a != 0:
    win32gui.SetActiveWindow(a)
    win32gui.BringWindowToTop(a)
    set_activeWindow(a)
    win32gui.MoveWindow(a, 200, 50, 392, 839, True)

# time.sleep(2)
#
# rect = win32gui.GetWindowRect(a)
# print(rect)
# ImageGrab.grab(rect).save("SC-03L_screenshot.png")
# print("get screenshot")

# pyautogui.mouseDown(920, 650, button='left')
# pyautogui.moveTo(920, 700, duration=0.1)
# pyautogui.moveTo(860, 700, duration=0.1)
# pyautogui.mouseUp(860, 700, button='left')
