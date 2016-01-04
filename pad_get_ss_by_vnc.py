# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import pyws as m
import ImageGrab
import winxpgui

def get_ss_by_pyws(device_name, filename):
    # get window handle
    hwnd = m.getid(device_name)
    # get window position
    rect = winxpgui.GetWindowRect(hwnd)
    # get window size
    size = winxpgui.GetClientRect(hwnd)
    # make list [x, y, w, h]
    cap = [rect[0],rect[1],size[2]+rect[0],size[3]+rect[1]]
    # capture
    img = ImageGrab.grab(cap)
    # save
    img.save(filename)

if __name__ == "__main__":
    device_name = "SH-01F"
    #device_name = "Nexus 7"
    filename = "screenshot_pyws.png"
    get_ss_by_pyws(device_name, filename)
