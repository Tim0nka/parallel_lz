import sys
import asyncio
import potok
import asynhron
import process
from multiprocessing import Process

def run_potok():
    potok.posled(potok.ips)
    potok.potoki(potok.ips)

async def run_asynhron():
    await asynhron.main()

def run_process():
    p = Process(target=process.main)
    p.start()
    p.join()