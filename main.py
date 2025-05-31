import sys
import asyncio
import potok
import asynhron
import process
from multiprocessing import Process

def pusk_potok():
    potok.posled(potok.ips)
    potok.potoki(potok.ips)

async def pusk_asynhron():
    await asynhron.main()

def pusk_process():
    p = Process(target=process.main)
    p.start()
    p.join()

if __name__ == "__main__":
    pusk_potok()
    asyncio.run(pusk_asynhron())
    pusk_process()
