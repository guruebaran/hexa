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


serialport.close()