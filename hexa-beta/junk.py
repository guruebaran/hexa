
sum = 0
dataSting = '0005010203041122334400b9'
for i in range(0,22):
    if( i%2 == 0):
        sum += int(dataSting[i:i+2],16)
checkSum = dataSting[22:24]
compv = hex(sum)[::-1]
print('compv[0:2][::-1]',compv[0:2][::-1])
if(compv[0:2][::-1] == checkSum):
    print('yo')
checkSum = int(dataSting[22:24],16)



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


data = (channel+command+param11+param12+param21+param22+dataSize11+dataSize12+dataSize21+dataSize22+errCode+'00')
print('qqqqqqqqqqq',data)

def xyz():
    return (1,'jkjk')

print('xyz',xyz()[1])