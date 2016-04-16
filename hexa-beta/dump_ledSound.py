__author__ = 'karthi'

import time
import asyncio
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT) # Red
GPIO.setup(11, GPIO.OUT) # Green
# buzzer
# light 2

GPIO.output(11,0)
GPIO.output(8,0)
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

def ledSoundFunction(putstate, colour):
    if putstate == 1:
        if colour == 1:
            GPIO.output(11, 1)
        if colour == 0:
            GPIO.output(8, 1)
    else:
        if colour == 1:
            GPIO.output(11, 0)
        if colour == 0:
            GPIO.output(8, 0)
