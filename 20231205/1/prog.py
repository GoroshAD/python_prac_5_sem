import asyncio

event = asyncio.Event()

async def writer(queue, delay):
    counter = 0
    await asyncio.sleep(delay)
    while True:
        await queue.put("{}_{}".format(counter, delay))
        counter += 1
        if event.is_set():
            break
        await asyncio.sleep(delay)

async def stacker(queue, stack):
    while True:
        item = await queue.get()
        await stack.put(item)
        if event.is_set():
            break

async def reader(stack, count, delay):
    await asyncio.sleep(delay)
    i = 0
    while i < count:
        item = await stack.get()
        print(item)
        i += 1
        await asyncio.sleep(delay)
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

