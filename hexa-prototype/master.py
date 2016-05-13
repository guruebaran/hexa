import os
import RPi.GPIO as GPIO
import database
import fpskbs as fps
import kbh
import Adafruit_CharLCD as LCD
from time import sleep
import string

lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #register
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #recharge
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pay
GPIO.setup(13, GPIO.OUT) #Add
GPIO.setup(19, GPIO.OUT) #Empty
GPIO.setup(26, GPIO.OUT) #Search

GPIO.output(13,1)
GPIO.output(19,1)
GPIO.output(26,1)



kb = kbh.KBHit()
global state
state = 0
i = 0
phn = []
amt = []
lcd.clear()
lcd.message("  Project Hexa\n Welcomes You!!")
lcd.show_cursor(True)
lcd.blink(True)

def registermode():
    lcd.clear()
    lcd.message('     Start \n  Registration')
    sleep(0.5)
    lcd.clear()
    lcd.message('Enter Phn Number\n>')
    global state
    state = 1

def rechargemode():
    lcd.clear()
    lcd.message("Deposit amt = ? \n Rs.")
    global state
    state = 2

def paymentmode():
    lcd.clear()
    lcd.message("Pay amt = ? \n Rs.")
    global state
    state = 3

while True:
    if kb.kbhit():
        x = kb.getch()
        if(state == 1):
            if(x.isdigit()):
                phn[++i] = x
                lcd.message(x)
                if(i == 9):
                    lcd.clear()
                    lcd.message('Touch to Proceed.')  # reponse time out check
                    GPIO.output(13,0)
                    sleep(0.05)
                    GPIO.output(13,1)
                    data = fps.readFPS()
                    if(int(data) == 0xFF):  # to be verified
                        lcd.clear()
                        lcd.message('Error...')
                    else:
                        lcd.clear()
                        lcd.message('Initial Deposit = ? \n Rs.')
                        bal = input()
                        lcd.message(str(bal))
                        database.reguser(int(data),phn,bal)  # check if int() is working
                        lcd.clear()
                        lcd.message('Your new Bal:\n Rs.',str(database.getbal(int(data))))
                        global status
                        state = 0
                        i = 0
                        sleep(4)
                        lcd.clear()
                        lcd.message("  Project Hexa\n Welcomes You!!")
        elif(state == 2):
            if ord(x) != 13:
                if(x.isdigit()):
                    amt[++i] = x
                    lcd.message(x)
            else:
                lcd.clear()
                lcd.message('Touch to Proceed.')  # response time out check
                GPIO.output(26,0)
                sleep(0.05)
                GPIO.output(26,1)
                data = fps.readFPS()
                if(int(data) == 0xFF):
                    lcd.clear()
                    lcd.message('Error...')
                else:
                    lcd.clear()
                    lcd.message('Updating...')
                    database.trans(int(data),int(amt),'+')
                    lcd.clear()
                    lcd.message('Your new Bal:\n Rs.',str(database.getbal(int(data))))
                    global status
                    status = 0
                    i = 0
                    sleep(4)
                    lcd.clear()
                    lcd.message("  Project Hexa\n Welcomes You!!")
        elif(state == 3):
            if ord(x) != 13:
                if(x.isdigit()):
                    amt[++i] = x
                    lcd.message(x)
            else:
                lcd.clear()
                lcd.message('Pay = Rs.',amt,' ?\nTouch to Proceed.') # reponse time out check
                GPIO.output(26,0)
                sleep(0.05)
                GPIO.output(26,1)
                data = fps.readFPS()
                if(int(data) == 0xFF):
                    lcd.clear()
                    lcd.message('Error...')
                else:
                    lcd.clear()
                    lcd.message('Paying...')
                    temp = database.trans(int(data),int(amt),'-')
                    if(temp == 0):
                        lcd.clear()
                        lcd.message('Insufficient Bal\nYour Bal: ',str(database.getbal(int(data))))
                    else:
                        lcd.clear()
                        lcd.message('Your new Bal:\n Rs.',str(database.getbal(int(data))))
                    global status
                    status = 0
                    i = 0
                    sleep(4)
                    lcd.clear()
                    lcd.message("  Project Hexa\n Welcomes You!!")
    if(GPIO.input(16) ==1):
        registermode()
    if(GPIO.input(20) ==1):
        rechargemode()
    if(GPIO.input(21) ==1):
        paymentmode()


GPIO.cleanup()
