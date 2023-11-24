import sys
fin = {'Size': 0, 'Type': 0, 'Channels': 0, 'Rate': 0, 'Bits': 0, 'Data size': 0}

def correct():
    if not sys.stdin.buffer.read(4).decode('utf-8') == 'RIFF':
        return False
    if t := sys.stdin.buffer.read(4):
        fin['Size'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    if not sys.stdin.buffer.read(4).decode('utf-8') == 'WAVE':
        return False
    sys.stdin.buffer.read(8)
    if t := sys.stdin.buffer.read(2):
        fin['Type'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    if t := sys.stdin.buffer.read(2):
        fin['Channels'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    if t := sys.stdin.buffer.read(4):
        fin['Rate'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    sys.stdin.buffer.read(6)
    if t := sys.stdin.buffer.read(2):
        fin['Bits'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    sys.stdin.buffer.read(4)
    if t := sys.stdin.buffer.read(4):
        fin['Data size'] = int.from_bytes(t, byteorder='little')
    else:
        return False
    return True

if correct():
    print(*[f"{i}={fin[i]}" for i in fin], sep=', ')
else:
    print('NO')
