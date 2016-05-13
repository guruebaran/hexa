import serial
import binascii
serialport = serial.Serial("/dev/ttyAMA0", timeout = 1)
serialport.baudrate = 9600
d="005001000000000000000051".decode("hex")
de="005100000000000000000051".decode("hex")
i="005600000000000000000056".decode("hex")
i="005600000000000000000056"
serialport.write(binascii.unhexlify(i))
print(binascii.hexlify(serialport.read(12)))
print(serialport.read(12))

bytes.fromhex('4a4b4c').decode('utf-8')
serialport.write(d)
serialport.write(binascii.unhexlify(i))
print(serialport.read(12))
print(serialport.read(12).encode("hex"))

clr="007600000000000000000076".decode("hex")
ai="00A1010000000000000000A2".decode("hex")
ais="00A2000000000000000000A2".decode("hex")

rc="004600000000000000000046".decode("hex")
ms="00F9000000000000000000F9".decode("hex")

clru = '0072ffff0000050000000075'
clrufp = '0054ffff0000050000000057'


getT = "004001000000000000000041"  # string res > 004001000000000000001051

i1 = "003500000000000000000035"
i2 = "003600000000000000000036"  # string res > 003600000000000000001046
i3 = "003700000000000000000037"  # string res > 003700000000fe090000003e
binascii.hexlify(serialport.read(2558)).decode("utf-8")

sl = "003008000000000000000038"


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP) # FPS Interrupt

def intr():
    print("hi1")
    i = 0
    t = time.time()
    while True:
        while GPIO.input(4) == 0:
            i += 1
            if time.time() - t > 1:
                i = 0
                t = time.time()
            print("hi>", i, ">>" ,time.time())



serialport.close()