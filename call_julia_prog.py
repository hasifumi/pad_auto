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
    #print("stdout_data:")
    #print(stdout_data)
    stdout_data = stdout_data.decode()
    #print("decoded:")
    #print(stdout_data)
    #print("len:"+str(len(stdout_data)))
    ary = []
    for i in range(int(len(stdout_data)/4)):
        #print("i:"+str(i))
        #print("out1:"+str(stdout_data[i]))
        #print("out2:"+str(stdout_data[i+2]))
        # ary.append([stdout_data[4*i]-1, stdout_data[4*i+2]-1])
        ary.append([int(stdout_data[4*i])-1, int(stdout_data[4*i+2])-1])
    # print ary
    return ary
