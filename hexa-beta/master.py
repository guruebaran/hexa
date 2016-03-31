import RPi.GPIO as GPIO
import database
import fpsDriver as fps
import idleScreen as ids
import miniStatementScreen as mss
import rechargeScreen as rs
import paymentScreen as ps
import userRegistrationScreen as urs
import kbh

fps.autoIdentifyStart()
mobileNumber = ""
state = 0
# state 0 - idle_Screen mode
# state 1 - registration mode
# state 2 - recharge mode
# state 3 - payment mode
# state 4 - ministatement mode


kb = kbh.KBHit()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # register
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # recharge
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # payment
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # back
GPIO.setup(04, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # FPS Interrupt
# buzzer
#light 2


def registermode():
    global state
    if state == 0:
        state = 1
        fps.autoIdentifyStop()
        urs.state40()

def rechargemode():
    global state
    state = 2

def paymentmode():
    global state
    state = 3

def miniStatementmode():
    global state
    state = 4


while True:
    if kb.kbhit():
        x = kb.getch()
        if state == 3:
            print("3")

        if state == 2:
            print("2")

        if state == 4:
            print("4")

        if state == 1:
            print("1")
            if urs.currentState == 40:
                if x.isdigit() or len(mobileNumber) < 10:
                    mobileNumber += x
                    urs.state40(mobileNumber)
                elif ord(x) == 127: # backspace
                    mobileNumber = mobileNumber[0:len(mobileNumber)-1]
                    urs.state40(mobileNumber)
                elif ord(x) == 13 or ord(x) == 10:
                    if len(mobileNumber) == 10:
                        if database.verifyMobileNumber()[0] == 0:#.........number alerady exists
                            urs.state61()
                        else: #.......not existing
                            urs.state100()
                            fps.autoIdentifyStart()
                                if fps.identify()[0] == 0:
                                    fps.autoIdentifyStop()
                                    if fps.initiateRegistration(mobileNumber)[0] == 1:
                                        urs.state30()
                                        if fps.terminateRegistration()[0] == 1:
                                            if fps.continueRegistration()[0] == 1:
                                                urs.state101()
                                                urs.autoIdentifyStart()
                                                if urs.identify()[0] == 0:
                                                    urs.autoIdentifyStop()
                                                    if fps.initiateRegistration(mobileNumber)[0] == 1:
                                                        urs.state30()
                                                        if fps.terminateRegistration()[0] == 1:
                                                            urs.state50()
                                                            if getTemplateGenerator(mobileNumber)[0] == 1:
                                                                #add template to the database
                                                                urs.state60()
                                                                #add money to account
                                                                urs.state70(phoneNumber,accountBalance)#parameters should be from database
                                                                sleep
                                                else:
                                                    print("poda panni")

                                else:
                                    print("poda panni")
            if urs.currentState == 61:
                if ord(x) == 13 or ord(x) == 10:
                    urs.state40()







    if GPIO.input(17) ==1:
        if state == 0:
            registermode()


    if GPIO.input(10) ==1:
        if state == 0:
            rechargemode()


    if GPIO.input(27) == 1:
        if state == 0:
            paymentmode()


    if GPIO.input(9) == 1:
        print('back')
    if GPIO.input(4) == 1:
        if state == 0:
            miniStatementmode()
        elif state == 3:

            print("payment mode")
        elif state == 2:

            print("recharge mode")
        elif state == 4:
            miniStatementmode()
        elif state == 1:
            print ("In register mode, Unexpected behavior")

#---------------------------------------------------------------------------------------------------------------------









database.conn.close()
GPIO.cleanup()