import serial

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

def readFPS():
    while True:
        data = serialport.read()
        return data