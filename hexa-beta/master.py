import RPi.GPIO as GPIO
import database
import fpsDriver as fps
import idleScreen as ids
import miniStatementScreen as mss
import rechargeScreen as rs
import paymentScreen as ps
import userRegistrationScreen as urs
import kbh
import time

fps.autoIdentifyStart()
mobileNumber = ""
amount = ""
fingerRegistrationGo = 0
screenTime = 0
state = 0
# state 0 - idle_Screen mode
# state 1 - registration mode
# state 2 - recharge mode
# state 3 - payment mode
# state 4 - ministatement mode
# state 5 - screen waiting


kb = kbh.KBHit()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # register
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # recharge
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # payment
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # back
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # FPS Interrupt



def registermode():
    global state
    if state == 0:
        state = 1
        fps.autoIdentifyStop()
        urs.state40()

def rechargemode():
    global state
    state = 2
    fps.autoIdentifyStop()


def paymentmode():
    global state
    state = 3
    fps.autoIdentifyStop()
    ps.state10()

def miniStatementmode():
    global state
    state = 4


while True:
    global state
    if kb.kbhit():
        x = kb.getch()
        if state == 3:
            print("3")
            if ps.currentState == 10:
                if x.isdigit() or len(amount) < 4:
                    amount += x
                    ps.state10(amount)
                elif ord(x) == 127:  # backspace
                    amount = amount[0:len(amount) - 1]
                    ps.state10(amount)
                elif ord(x) == 13 or ord(x) == 10:
                    ps.state20(amount)
                    fps.autoIdentifyStart()




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
                                    fingerRegistrationGo = 0
                                    while fingerRegistrationGo == 0:
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
                                                                else:
                                                                    print ("template fetch error")
                                                            else:
                                                                print("terminate reg failed")
                                                        else:
                                                            print ("initiate reg failed")
                                                    else:
                                                        print("poda panni")
                                                        break
                                                else:
                                                    print("continue reg failed")
                                            else:
                                                print("terminate reg failed")
                                        else:
                                            print("initiate failed")

                                else:
                                    print("poda panni")
            if urs.currentState == 61:
                if ord(x) == 13 or ord(x) == 10:
                    urs.state40()
            if urs.currentState == 60:
                if x.isdigit() or len(amount) < 4:
                    amount += x
                    urs.state60(amount)
                elif ord(x) == 127:  # backspace
                    amount = amount[0:len(amount) - 1]
                    urs.state60(amount)
                elif ord(x) == 13 or ord(x) == 10:
                    database.registerUser (mobileNumber, int(amount), 1001) # add money to account
                    urs.state70(mobileNumber, database.getbal(mobileNumber))  # parameters should be from database
                    urs.currentState = 0
                    amount = ""
                    mobileNumber = ""
                    state = 5
                    screenTime = time.time()



    elif GPIO.input(17) == 1:
        if state == 0 or state == 5:
            registermode()


    elif GPIO.input(10) == 1:
        if state == 0 or state == 5:
            rechargemode()


    elif GPIO.input(27) == 1:
        if state == 0 or state == 5:
            paymentmode()


    elif GPIO.input(9) == 1:
        print('back')

    elif GPIO.input(4) == 1:
        if state == 0 or state == 5:
            miniStatementmode()
        elif state == 3:
            print("fps interrupt in payment mode")
            ps.state30()
            fres = fps.identify()
            if fres[0]:
                fps.autoIdentifyStop()
                if trans(mobileNumber, int(amount), '-', 1001):
                    ps.state40()
                else:
                    ps.state32()
            else:
                ps.state31()
                state = 5
                ps.currentState = 0
                amount = ""
                mobileNumber = ""
                screenTime = time.time()


        elif state == 2:

            print("fps interrupt in recharge mode")
        elif state == 4:
            miniStatementmode()
        elif state == 1:
            print ("fps interrupt in register mode, Unexpected behavior")

    elif state == 5:
        if screenTime - time.time() > 5:
            screenTime = 0
            state = 0
            ids.state10()



#---------------------------------------------------------------------------------------------------------------------






database.conn.close()
GPIO.cleanup()