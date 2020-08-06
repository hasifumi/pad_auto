import subprocess

def call_julia_prog(board="315211554451322114424566531621", width=6, height=5, debug_flg=0, eval_param="", max_turn=50, beam_width=800):

    command = "julia pd_combo.jl "+board+" "+str(width)+" "+str(height)+" "+str(debug_flg)+" "+str(eval_param)+" "+str(max_turn)+" "+str(beam_width)
    print(command)

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
