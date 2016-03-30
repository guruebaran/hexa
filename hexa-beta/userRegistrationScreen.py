__author__ = 'guru'


#state 40 = enter the phone number
#state 61 = phone number already exist try new number
#state 10 = Ask's user to place their finger on FPS
#state 20 = Scanning ur finger now
#state 30 = remove ur finger and place it again
#state 41 = sorry user fingerprint already exists
#state 50 = processing please wait
#state 60 = initial deposit info
#state 70 = Full info

#screen = 0 vendor,screen = 1 customer.

import GLCD as g

currentState = 0
fontWidth = 6
lineLength = 21


def state40(phoneNumber = ' '):
    global currentState
    currentState = 40
    #vendor Screen
    string = ("{:.^%d}" % lineLength).format("PLEASE ENTER THE")
    g.displayText(string,2,0,0)
    string = ("{:.^%d}" % lineLength).format("PHONE NUMBER")
    g.displayText(string,3,0,0)
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,4,0,0)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,4,(6*fontWidth-1),0)
    #user Screen
    g.clearDisplay()
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,4,0,1)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,4,(6*fontWidth-1),1)


def state61():
    global currentState
    currentState = 61
    #vendor Screen

    string = ("{:.^%d}" % lineLength).format("PHONE NUMBER IS")
    g.displayText(string,3,0,0)
    string = ("{:.^%d}" % lineLength).format("ALREADY REGD")
    g.displayText(string,4,0,0)


    #User Screen
    string = ("{:.^%d}" % lineLength).format("IT SEEMS THE ")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("PHONE NUMBER IS")
    g.displayText(string,3,0,1)
    string = ("{:.^%d}" % lineLength).format("ALREADY REGD")
    g.displayText(string,4,0,1)
    string = ("{:.^%d}" % lineLength).format("TRY A NEW NUMBER")
    g.displayText(string,5,0,1)


def state10():
    global currentState
    currentState = 10
    #vendor Screen
    g.clearDisplay()
    string = ("{:.^%d}" % lineLength).format("REGISTERING")
    g.displayText(string,0,0,0)
    string = ("{:.^%d}" % lineLength).format("WAITING FOR FINGER")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay()
    string = ("{:.^%d}" % lineLength).format("REGISTERING")
    g.displayText(string,0,0,1)
    string = ("{:.^%d}" % lineLength).format("PLACE UR FINGER")
    g.displayText(string,3,0,1)


def state20():
    global currentState
    currentState = 20
    #vendor Screen
    g.clearDisplay()
    string = ("{:.^%d}" % lineLength).format("SCANNING USER'S")
    g.displayText(string,2,0,0)
    string = ("{:.^%d}" % lineLength).format("FINGER NOW")
    g.displayText(string,3,0,0)
    #User Screen
    string = ("{:.^%d}" % lineLength).format("SCANNING YOUR")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("FINGER NOW")
    g.displayText(string,3,0,1)


def state30():
    global currentState
    currentState = 30
    #vendor Screen

    #User Screen

    string = ("{:.^%d}" % lineLength).format("REMOVE UR FINGER")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("AND")
    g.displayText(string,3,0,1)
    string = ("{:.^%d}" % lineLength).format("PLACE IT AGAIN")
    g.displayText(string,4,0,1)


def state41():
    global currentState
    currentState = 41
    #vendor Screen

    string = ("{:.^%d}" % lineLength).format("FINGER PRINT")
    g.displayText(string,3,0,0)
    string = ("{:.^%d}" % lineLength).format("ALREADY EXISTS")
    g.displayText(string,4,0,0)
    #User Screen
    string = ("{:.^%d}" % lineLength).format("SORRY")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("FINGER PRINT")
    g.displayText(string,3,0,1)
    string = ("{:.^%d}" % lineLength).format("ALREADY EXISTS")
    g.displayText(string,4,0,1)


def state50():
    global currentState
    currentState = 50
    #vendor Screen
    string = ("{:.^%d}" % lineLength).format("PROCESSING")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("PLEASE WAIT")
    g.displayText(string,3,0,1)

    #User Screen
    string = ("{:.^%d}" % lineLength).format("PROCESSING")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("PLEASE WAIT")
    g.displayText(string,3,0,1)


def state60(accountBalance):
    global currentState
    currentState = 60
    #vendor Screen
    string = ("{:.^%d}" % lineLength).format("DEPOSITE AMOUNT")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,4,0,0)
    g.displayText(accountBalance,4,(3*fontWidth-1))

    #User Screen
    string = ("{:.^%d}" % lineLength).format("HOW MUCH DO")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("YOU LIKE")
    g.displayText(string,3,0,1)
    string = ("{:.^%d}" % lineLength).format("TO DEPOSITE")
    g.displayText(string,4,0,1)


def state70(phoneNumber"0000000000",accountBalance="000.00"):
    #vendor Screen
    string = ("{:.^%d}" % lineLength).format("REGISTRATION")
    g.displayText(string,1,0,0)
    string = ("{:.^%d}" % lineLength).format("SUCCESSFULL")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,4,0,0)
    g.displayText(phoneNumber,4,(6*fontWidth-1))
    string = ("{:.<%d}" % lineLength).format("BALANCE:Rs.")
    g.displayText(string,5,0,1)
    g.displayText(accountBalance,5,(11*fontWidth-1))

    #User Screen
    g.clearDisplay()
    string = ("{:.^%d}" % lineLength).format("YOU HAVE")
    g.displayText(string,0,0,1)
    string = ("{:.^%d}" % lineLength).format("SUCCESSFULLY")
    g.displayText(string,1,0,1)
    string = ("{:.^%d}" % lineLength).format("REGISTERED")
    g.displayText(string,2,0,1)
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,4,0,1)
    g.displayText(phoneNumber,4,(6*fontWidth-1))
    string = ("{:.<%d}" % lineLength).format("BALANCE:Rs.")
    g.displayText(string,5,0,1)
    g.displayText(accountBalance,5,(11*fontWidth-1))
    string = ("{:.^%d}" % lineLength).format("THANK YOU")
    g.displayText(string,7,0,1)