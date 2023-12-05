import asyncio

async def squarer(p):
    return p*p

async def doubler(p):
    return p+p

arr = [1,2]
async def main(*args):
    res = await asyncio.gather(*(squarer(arg) for arg in args))
    res = await asyncio.gather(*(doubler(arg) for arg in res))
    print(*res)

asyncio.run(main(*arr))
