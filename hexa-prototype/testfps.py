import RPi.GPIO as GPIO
import fps as fps
import kbh
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) #Add
GPIO.setup(23, GPIO.OUT) #search
GPIO.setup(24, GPIO.OUT) #empty

GPIO.output(18,1)
GPIO.output(23,1)
GPIO.output(24,1)

while true:
    x = input('Enter a choice: \n1.Register\n2.search \n3.empty \nEsc to Exit ')
    if (x == '1'):
        GPIO.output(18,0)
        sleep(0.05)
        GPIO.output(18,1)
        data = fps.readFPS()
        print("data(raw) = ",data,"data(int) = ",int(data))

    elif (x == '2'):
        GPIO.output(18,0)
        sleep(0.05)
        GPIO.output(18,1)
        data = fps.readFPS()
        print("data(raw) = ",data,"data(int) = ",int(data))

    elif (x == '3'):
        GPIO.output(18,0)
        sleep(0.05)
        GPIO.output(18,1)
        data = fps.readFPS()
        print("data(raw) = ",data,"data(int) = ",int(data))

