import subprocess

# command = "julia pd_combo.jl 315211554451322114424566531621"

command = "julia pd_combo.jl 315211554451322114424566531621 6 5"

# command = "julia pd_combo.jl 251152214335411145466646655524351443131665 7 6"

proc = subprocess.Popen(
        command,
        shell = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        )

stdout_data, stderr_data = proc.communicate()
print stdout_data
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
print ary
# a = eval(stdout_data_connect)
# print(type(a))
