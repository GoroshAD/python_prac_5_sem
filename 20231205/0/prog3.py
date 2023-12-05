import asyncio, math

async def prod(num, q1):
    for i in range(5):
        await asyncio.sleep(1)
        val = f"{num}:{i}"
        await q1.put(val)
        print(f"Put {val}")

async def mid(num, q1, q2):
    for i in range(10000000000000000000000000000000000000000000000000000000000000000):
        await asyncio.sleep(1)
        res = await q1.get()
        print(f"\tGot {res}")
        val = f"{num}:{i}"
        await q1.put(val)
        print(f"Put {val}")

async def cons(q2):
    for i in range(10000000000000000000000000000000000000000000000000000000000000000):
        await asyncio.sleep(1)
        res = await q2.get()
        print(f"\tGot {res}")

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    await asyncio.gather(
            prod(1, q1),
            mid(2, q1, q2),
            cons(q2))

asyncio.run(main())
