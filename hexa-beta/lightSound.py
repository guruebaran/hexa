__author__ = 'guru'
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.OUT) #buzzer
GPIO.setup(11,GPIO.OUT) #red
interrupt = 0
flagtime = 0

def lightAndSound():
    global flagtime
    flagtime = time.time()
    global interrupt
    while interrupt != 1:
        if kb.kbhit() or GPIO.input(4) == 0 or GPIO.input(9) == 0 or GPIO.input(27) == 0 or GPIO.input(10) == 0 or GPIO.input(17) == 0:
            interrupt = 0
        else:
            GPIO.output(8,True)
            GPIO.output(11,True)

            if time.time()-flagtime > 0.1:

                GPIO.output(8,False)
                GPIO.output(11,False)
                flagtime = time.time()
    else:
        break
