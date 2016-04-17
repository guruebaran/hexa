__author__ = 'guru'

#state 10 = Ask's user to place their finger on FPS
#state 20 = Scanning ur finger now
#state 21 = Acccount not found
#state 30 = Mini Statement(last 3 transcations)


#screen = 0 vendor,screen = 1 customer.

import GLCD as g

currentState = 0

fontWidth = 6
lineLength = 21


def state10():
    global currentState
    currentState = 10
    #vendor Screen
    g.clearDisplay(0)

    string = ("{:^%d}" % lineLength).format("Waiting For Finger")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("Place Ur Finger")
    g.displayText(string,3,0,1)




def state20():
    global currentState
    currentState = 20
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:^%d}" % lineLength).format("Scanning User's")
    g.displayText(string,2,0,0)
    string = ("{:^%d}" % lineLength).format("Finger...")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("Scanning Your")
    g.displayText(string,2,0,1)
    string = ("{:^%d}" % lineLength).format("Finger...")
    g.displayText(string,3,0,1)


def state21():
    global currentState
    currentState = 21
    #vendor Screen

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("OOPS!")
    g.displayText(string, 3, 0, 1)
    string = ("{:^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,5,0,1)



def state30(phoneNumber):
    global currentState
    currentState = 30
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:^%d}" % lineLength).format("MINI-STATEMENT")
    g.displayText(string,0,0,0)
    string = ("{:<%d}" % lineLength).format("Mob.No:")
    g.displayText(string,1,0,0)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,1,(7*fontWidth-1),0)
    string = ("{:^%d}" % lineLength).format(" DATE    VNU P/R  AMT")
    g.displayText(string,2,0,0)

    #user Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("MINI-STATEMENT")
    g.displayText(string,0,0,1)
    string = ("{:<%d}" % lineLength).format("Mob.No:")
    g.displayText(string,1,0,1)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,1,(7*fontWidth-1),0)
    string = ("{:^%d}" % lineLength).format(" DATE    VNU P/R  AMT")
    g.displayText(string,2,0,1)


def state30Trans(date, transcationPoint, plusMinus, amount, TransNum):
    global currentState
    currentState = 30
    linenum = 3 + TransNum
    # vendor Screen
    string = "{:<8}".format(date)
    g.displayText(string, linenum,0,0)
    string = "{:<4}".format(transcationPoint)
    g.displayText(string, linenum,9,0)
    string = "{:<1}".format(plusMinus)
    g.displayText(string, linenum,13,0)
    string = "{:<4}".format(amount)
    g.displayText(string, linenum,17,0)


    # user Screen
    string = "{:<8}".format(date)
    g.displayText(string, linenum,0,1)
    string = "{:<4}".format(transcationPoint)
    g.displayText(string, linenum,9,1)
    string = "{:<1}".format(plusMinus)
    g.displayText(string, linenum,13,1)
    string = "{:<4}".format(amount)
    g.displayText(string, linenum,17,1)