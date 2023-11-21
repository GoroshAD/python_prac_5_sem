f = open("cal", "rb")
help(f.read)
while b:= f.read(1):
    print(b, end=" ")


f = open("cal", "rb")
while b:= f.read(1):
    print(b[0], end = " ")
print()


with open("cal", "rb") as f:
    while b:= f.read(1):
        print(hex(b[0]), end= "")
    print()
with open("cal", "rb") as f:
    while b:=f.read(1):
        print(f"{b[0]:08b}")
    print()

import pathlib
f.seek(2)
f.seek(0, 2)
f.seek(0)
