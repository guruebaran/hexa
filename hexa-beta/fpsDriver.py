__author__ = 'guru'
import serial
import binascii
serialport = serial.Serial("/dev/ttyAMA0", timeout=0.5)
serialport.baudrate = 9600

def fpsTransmitter(data):
    question =  binascii.unhexlify(data)
    serialport.write(question)

def fpsReceiver():
    return binascii.hexlify(serialport.read(12)).decode("utf-8")

def checkSum(dataString,write):
    totalSum = 0
    for i in range(0,22):
        if( i%2 == 0):
            totalSum += int(dataString[i:i+2],16)
    checkSum = dataString[22:24]
    tempString = hex(totalSum)[::-1]     #[::-1] reverses the string
    if((tempString[0:2][::-1] == checkSum) or (write == 1)):
        chkString = tempString[0:2][::-1]
        return (1,chkString)
    else:
        chkString = '0'
        return (0,chkString)

def dataCompiler(channel,command,param11,param12,param21,param22,dataSize11,dataSize12,dataSize21,dataSize22,errCode):
    All = (channel+command+param11+param12+param21+param22+dataSize11+dataSize12+dataSize21+dataSize22+errCode+'00')
    temp = checkSum(All,1)
    if( temp[0] == 1):
        All = All[0:22]
        All+=temp[1]
        return All
    else:
        return 0

def registrationDataGenerator():
def verificationDataGenerator():
def getTemplateGenerator():
def extraDataGenerator():
