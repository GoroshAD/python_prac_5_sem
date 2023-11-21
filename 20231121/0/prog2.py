with open("cal", "r") as f:
    b = f.read()

with open("cal2", "w") as f:
    f.write(b[:len(b) // 3 + b[len(b) // 3 - 1].find('\n')])
