fir, sec = 0, 0
b = []
with open("cal", "rb") as f:
    b = f.read()
    fir = len(b) // 2
    sec = len(b) - fir
with open("cal", "wb") as f:
    f.write(b[sec:])
    f.write(b[:fir])
