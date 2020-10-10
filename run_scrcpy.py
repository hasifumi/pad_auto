# -*- coding: utf-8 -*-

import subprocess

GALAXY_IP = "192.168.1.74"
AQUOS_SHV32_IP = "192.168.1.24"
FIREHD8_IP = "192.168.1.43"

print("select android (1: galaxy s10,  2: aquos shv32, 3: kindle fire hd8 ... else:default(galaxy s10) )")
input_test_word = input(">>>  ")
input_test_word = int(input_test_word)
#print("input_test_word:"+input_test_word)
#print("type:"+str(type(input_test_word)))
if input_test_word == 1:
    command_adb_connect = ["adb", "connect", GALAXY_IP ]
    command_scrcpy = ["C:\\Program Files\\scrcpy\\scrcpy.exe", "-s "+GALAXY_IP+":5555", "-b2M", "-m800"]
elif input_test_word == 2:
    command_adb_connect = ["adb", "connect", AQUOS_SHV32_IP ]
    command_scrcpy = ["C:\\Program Files\\scrcpy\\scrcpy.exe", "-s "+AQUOS_SHV32_IP+":5555", "-b2M", "-m800"]
elif input_test_word == 3:
    command_adb_connect = ["adb", "connect", FIREHD8_IP]
    command_scrcpy = ["C:\\Program Files\\scrcpy\\scrcpy.exe", "-s "+FIREHD8_IP+":5555", "-b2M", "-m800"]
else:
    #print("else:")
    command_adb_connect = ["adb", "connect", GALAXY_IP ]
    command_scrcpy = ["C:\\Program Files\\scrcpy\\scrcpy.exe", "-s "+GALAXY_IP+":5555", "-b2M", "-m800"]

subprocess.call(command_adb_connect)
# subprocess.call(command_scrcpy)
subprocess.Popen(command_scrcpy)

