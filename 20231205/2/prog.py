import asyncio, random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())
    i, j, k = start, middle, start
    while i < middle or j < finish:
        if j == finish or (i < middle and A[i] < A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    event_out.set()

async def mtasks(A):
    tmp_A, B = A.copy(), [0] * len(A)
    tasks, event_arr = [], []

    for i in range(len(tmp_A) + 1):
        event_arr.append(asyncio.Event())
        event_arr[i].set()

    leng, flag = 1, True
    while leng < len(tmp_A):
        tmp_event_arr, i = [], 0
        for start in range(0, len(A), leng * 2):
            middle, finish = min(start + leng, len(tmp_A) - 1), min(start + leng * 2, len(tmp_A))
            tmp_event_arr.append(asyncio.Event())

            if flag:
                tasks.append(asyncio.create_task(merge(tmp_A, B, start, middle, finish, event_arr[i], event_arr[i + 1], tmp_event_arr[-1])))
            else:
                tasks.append(asyncio.create_task(merge(B, tmp_A, start, middle, finish, event_arr[i], event_arr[i + 1], tmp_event_arr[-1])))
            i += 2
            if finish == len(tmp_A):
                break

        tmp_event_arr.append(tmp_event_arr[-1])
        event_arr = tmp_event_arr
        flag = False if flag else True
        leng *= 2 

    return (tasks, tmp_A) if flag else (tasks, B)


import sys
exec(sys.stdin.read())