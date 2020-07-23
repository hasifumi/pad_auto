import subprocess

def call_julia_prog(board="315211554451322114424566531621"):

    command = "julia pd_combo.jl " + board

    proc = subprocess.Popen(
            command,
            shell = True,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            )

    stdout_data, stderr_data = proc.communicate()
    ary = []
    for i in range(len(stdout_data)/4):
        ary.append([int(stdout_data[4*i])-1, int(stdout_data[4*i+2])-1])
    # print ary
    return ary
