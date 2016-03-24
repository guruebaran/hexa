__author__ = 'guru'
import binascii
dataSting = '0005010203041122334400b9'
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

a = checkSum(dataSting,0)
if( a == 1):
    print('yo',a[1])

channel = dataSting[0:2]
command = dataSting[2:4]
param11= dataSting[4:6]
param12= dataSting[6:8]
param21= dataSting[8:10]
param22 =dataSting[10:12]
dataSize11=dataSting[12:14]
dataSize12=dataSting[14:16]
dataSize21=dataSting[16:18]
dataSize22=dataSting[18:20]
errCode = dataSting[20:22]


def dataCompiler(channel,command,param11,param12,param21,param22,dataSize11,dataSize12,dataSize21,dataSize22,errCode):
    All = (channel+command+param11+param12+param21+param22+dataSize11+dataSize12+dataSize21+dataSize22+errCode+'00')
    temp = checkSum(All,1)
    if( temp[0] == 1):
        All = All[0:22]
        All+=temp[1]
        new = temp[0]
        return All
    else:
        return 0


final = dataCompiler(channel,command,param11,param12,param21,param22,dataSize11,dataSize12,dataSize21,dataSize22,errCode)
print('wow',final)

