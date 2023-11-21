import random 
import struct 
import sys 

b = b"abc"
n = random.randrange(1000000)
fl = random.random()
for fmt, name in [("<f3si", sys.argv[1]), ("!f3si", sys.argv[2])]:
    with open(name, "wb") as f:
        for i in range(10):
            f.write(struct.pack(fmt, fl, bytes(b), n))
