# -*- coding: utf-8 -*-
# vim:set foldmethod=marker:

import subprocess
import time

device_path = "/sdcard/screenshot.png"
path = ".\screenshot.png"

WIDTH = 6
HEIGHT = 5

def get_screenshot(device_path):# {{{
    screencap_cmd = ["adb", "shell", "screencap", device_path]
    subprocess.check_call(screencap_cmd, shell=True)

    pull_cmd = ["adb", "pull", device_path]
    subprocess.check_call(pull_cmd, shell=True)

    return# }}}

def getting_screenshot(device_path, path, WIDTH, HEIGHT, use_old=0):# {{{
    if use_old == 0:
        print("getting screenshot ...")
        start_time = time.time()
        get_screenshot(device_path)
    else:
        print("using old screenshot ...")
        start_time = time.time()

    elapsed_time = time.time() - start_time
    print("getting time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    getting_screenshot(device_path, path, WIDTH, HEIGHT)

