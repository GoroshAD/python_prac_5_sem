import asyncio

event = asyncio.Event()

async def writer(queue, delay):
    counter = 0
    while True:
        await asyncio.sleep(delay)
        await queue.put("{}_{}".format(counter, delay))
        counter += 1
        if event.is_set():
            break

async def stacker(queue, stack):
    while True:
        await asyncio.sleep(0)
        try:
            item = queue.get_nowait()
            await stack.put(item)
        except:
            pass
        if event.is_set():
            break

async def reader(stack, count, delay):
    i = 0
    while i < count:
        await asyncio.sleep(delay)
        try:
            item = stack.get_nowait()
            print(item)
            i += 1
        except:
            continue
    event.set()

async def main(delay1, delay2, delay3, count):
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, count, delay3)
    )

delay1, delay2, delay3, count = eval(input())
asyncio.run(main(delay1, delay2, delay3, count))

