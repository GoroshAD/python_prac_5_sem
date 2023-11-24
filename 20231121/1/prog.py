import sys

n = sys.stdin.buffer.read(1)
t = sys.stdin.buffer.read()
rest = len(t)
num = abs(n[0])

arr = [round((i * rest) / num) for i in range(num)]
arr.append(rest)
fin = [t[arr[i]:arr[i + 1]] for i in range(num)]
fin.sort()

sys.stdout.buffer.write(n + b''.join(fin))
