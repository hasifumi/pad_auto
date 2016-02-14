import os
f = open("abspath","w")
f.write(os.path.dirname(__file__))
