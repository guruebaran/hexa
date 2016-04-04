__author__ = 'karthi'

import time
import asyncio
import datetime

def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()
for a in display_date(loop):
    print("hi", a)
loop.close()