import subprocess
import time

# command = "julia pd_combo.jl 315211554451322114424566531621"

command = "julia pd_combo.jl 315211554451322114424566531621 6 5 0"
# ARGS 1:field, 2:ROW, 3:COL, 4:debug_flg(0:off, 1:on), 5:eval_param(1:delete_row, ...)

# command = "julia pd_combo.jl 315211554451322114424566531621 6 5 1"

# command = "julia pd_combo.jl 251152214335411145466646655524351443131665 7 6"

start_time = time.time()

proc = subprocess.Popen(
        command,
        shell = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        )

stdout_data, stderr_data = proc.communicate()

elapsed_time = time.time() - start_time
print("test2:{} [sec]".format(elapsed_time))# }}}

print(stdout_data)
# print stderr_data
# print(len(stdout_data))
# stdout_data_connect = ""
# len1 = len(stdout_data) / 4
# print len1
ary = []
#for i in range(len(stdout_data)/4):
#    ary.append([int(stdout_data[4*i])-1, int(stdout_data[4*i+2])-1])
    # stdout_data_connect = stdout_data_connect + i
# print stdout_data_connect
# print(len(stdout_data_connect))
# # print(len(stdout_data_connect))
print(ary)
# a = eval(stdout_data_connect)
# print(type(a))
