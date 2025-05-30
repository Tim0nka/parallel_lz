import asyncio
import time
import random

number = 1

async def fun1():
    global number
    jump = random.randint(1,10)
    number=+-jump
    await asyncio.sleep(0.1)
    print(number)
    


async def fun2(x):
    print(random.randint(1,10))
    await asyncio.sleep(0.1)
    



async def main():
    print(random.randint(1,10))
    await asyncio.sleep(0.1)
    


    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))