__author__ = 'guru'
import serial
import binascii
serialport = serial.Serial("/dev/ttyAMA0", timeout=0.5)
serialport.baudrate = 9600

def fpsTransmitter(data):
    question =  binascii.unhexlify(data).encode("utf-8")
    serialport.write(question)

def fpsReceiver():
    return binascii.hexlify(serialport.read(12)).decode("utf-8")

def checksum(dataString):
