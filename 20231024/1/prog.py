def fib(m, n) :
    arr = [1, 1]
    for i in range(2, m + 1) :
        arr.append(arr[i - 1] + arr[i - 2])
    counter = 0
    while counter < n :
        yield arr[m]
        if m > 0 :
            arr.append(arr[m] + arr[m - 1])
        m += 1
        counter += 1



import sys
exec(sys.stdin.read())
