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
import binascii

fps.autoIdentifyStart()
mobileNumber = ""
amount = ""
fingerRegistrationGo = 0
screenTime = 0
state = 0
interrupt = 0
flagtime = 0
# state 0 - idle_Screen mode
# state 1 - registration mode
# state 2 - recharge mode
# state 3 - payment mode
# state 4 - ministatement mode
# state 5 - screen waiting


kb = kbh.KBHit()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP) # register
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP) # recharge
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP) # payment
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_UP) # back
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP) # FPS Interrupt
GPIO.setup(8,GPIO.OUT) #buzzer
GPIO.setup(11,GPIO.OUT) #red

def registermode():
    global state
    state = 1
    fps.autoIdentifyStop()
    urs.state40()

def rechargemode():
    global state
    state = 2
    fps.autoIdentifyStop()
    rs.state10()


def paymentmode():
    global state
    state = 3
    fps.autoIdentifyStop()
    ps.state10()



def miniStatementmode():
    global state
    state = 4
    mss.state30()

def blink():
    global flagtime
    flagtime = time.time()
    global interrupt
    while interrupt != 1:
        if kb.kbhit() or GPIO.input(4) == 0 or GPIO.input(9) == 0 or GPIO.input(27) == 0 or GPIO.input(10) == 0 or GPIO.input(17) == 0:
            interrupt = 0
        else:
            GPIO.output(8,True)
            GPIO.output(11,True)

            if time.time()-flagtime > 0.25:

                GPIO.output(8,False)
                GPIO.output(11,False)
                flagtime = time.time()
    else:
        break


while True:
    global state
    if kb.kbhit():
        x = kb.getch()
        if state == 0 or state == 5:
            if x == '1':
                registermode()
            elif x == '2':
                rechargemode()
            elif x == '3':
                paymentmode()
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
                    while True:
                        if GPIO.input(4) == 0:
                            print("fps interrupt in payment mode")
                            ps.state30()
                            fres = fps.identify()
                            if fres[0]:
                                fps.autoIdentifyStop()
                                transr = database.trans(fres[1], int(amount), '-', 1001)
                                if transr[0] == 1:
                                    ps.state40(amount)
                                else:
                                    ps.state32(transr[1])
                                break
                            else:
                                ps.state31()
                                break
                        elif GPIO.input(9) == 0:
                            ids.state10()
                            break
                    state = 5
                    ps.currentState = 0
                    amount = ""
                    mobileNumber = ""
                    screenTime = time.time()





        if state == 2:
            print("2")
            if rs.currentState == 10:
                if x.isdigit() or len(amount) < 4:
                    amount += x
                    rs.state10(amount)
                elif ord(x) == 127:  # backspace
                    amount = amount[0:len(amount) - 1]
                    rs.state10(amount)
                elif ord(x) == 13 or ord(x) == 10:
                    rs.state20(amount)
                    fps.autoIdentifyStart()
                    while True:
                        if GPIO.input(4) == 0:
                            print("fps interrupt in recharge mode")
                            rs.state30()
                            fres = fps.identify()
                            if fres[0]:
                                fps.autoIdentifyStop()
                                transr = database.trans(fres[1], int(amount), '+', 1001)
                                if transr[0]:
                                    rs.state40(amount, transr[1])
                                else:
                                    rs.state31() # "fatal" exeption to be handled
                            else:
                                rs.state31()
                                break
                        elif GPIO.input(9) == 0:
                            ids.state10()
                            break
                    state = 5
                    rs.currentState = 0
                    amount = ""
                    mobileNumber = ""
                    screenTime = time.time()



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
                            while True:
                                if GPIO.input(4) == 0:
                                    if fps.identify()[0] == 0:
                                        fps.autoIdentifyStop()
                                        fingerRegistrationGo = 0
                                        while fingerRegistrationGo == 0:


                                            if fps.doubleRegistration()[0] == 1:
                                                if fps.initiateRegistration(mobileNumber)[0] == 1:
                                                    urs.state30()
                                                    if fps.terminateRegistration()[0] == 1:
                                                        urs.state50()
                                                        if urs.getTemplateGenerator(mobileNumber)[0] == 1:
                                                            tempOne =  binascii.unhexlify(urs.getTemplateGenerator(mobileNumber)[1])
                                                            tempTwo =  binascii.unhexlify(urs.getTemplateGenerator(mobileNumber)[2])
                                                            database.storeTemplate(mobileNumber, tempOne, tempTwo)

                                                            urs.state60()
                                                            fingerRegistrationGo = 1

                                                        else:
                                                            print ("template fetch error")
                                                    else:
                                                        print("terminate reg failed")
                                                else:
                                                    print ("initiate reg failed")
                                            else:
                                                print("double registration ack failed")
                                        break
                                    else:
                                        print("poda panni")
                                elif GPIO.input(9) == 0:
                                    break  # handle

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



    elif GPIO.input(17) == 0:
        if state == 0 or state == 5:
            registermode()


    elif GPIO.input(10) == 0:
        if state == 0 or state == 5:
            rechargemode()


    elif GPIO.input(27) == 0:
        if state == 0 or state == 5:
            paymentmode()


    elif GPIO.input(9) == 0:
        print('back')

    elif GPIO.input(4) == 0:
        if state == 0 or state == 5:
            miniStatementmode()
        elif state == 4:
            data = fps.identify()
            if data[0] == 1:
                mobileNumber = data[1]
                mss.state30(mobileNumber)
                dispData = mss.getLastTransactions(mobileNumber,3)
                for i in range(1,3):
                    tDate = dispData[i][3][5:7]+'/'+dispData[i][3][8:10]+'/'+dispData[i][3][2:4]
                    tPoint = str(dispData[i][4])
                    mss.state30Trans(tDate, tPoint, dispData[i][2], str(dispData[i][5]), i-1)

            else:
                print ("FPS not found")
                mss.state21()
            while True:
                if GPIO.input(4) == 1:
                    break
            ids.state10()
            state = 0
            mss.currentState = 0
            amount = ""
            mobileNumber = ""


    elif state == 5:
        if time.time() - screenTime > 5:
            screenTime = 0
            state = 0
            amount = ""
            mobileNumber = ""
            ids.state10()



#---------------------------------------------------------------------------------------------------------------------






database.conn.close()
database.cursor.close()
GPIO.cleanup()
fps.serialport.close()
