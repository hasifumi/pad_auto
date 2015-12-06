import subprocess

#subprocess.check_call(['ls', '-l'], shell=True)
#subprocess.check_call(['pwd'], shell=True)
#subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/sample2.exe", '111', '2222'], shell=True)

board = "111112222233333444445555566666"
p = subprocess.Popen(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], stdout=subprocess.PIPE)
#subprocess.check_call(["c:/Users/fumio/MyProject/python/pad_auto/ref/pazdra_kun.exe", board], shell=True)
sout = []
while 1:
    c = p.stdout.readline()
    if not c:
        break
    #print c
    sout.append(c.rstrip())
p.wait()
print sout
