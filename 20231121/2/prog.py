import sys
print(sys.stdin.buffer.read().decode('utf-8', errors='replace').encode('latin1', errors='replace').decode('cp1251', errors='replace'))
