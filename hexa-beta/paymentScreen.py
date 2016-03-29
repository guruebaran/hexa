__author__ = 'guru'
#state 10 = payment amount
#state 20 = Ask's user to place their finger on FPS
#state 30 = Scanning ur finger now
#state 31 = account not found
#state 32 = no enough balance
#state 40 = payment successful

#screen = 0 vendor,screen = 1 customer.

import GLCD as g

currentState = 0
fontWidth = 6
lineLength = 21


def state10(paymentAmount):
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("PAYMENT AMOUNT")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)

    g.displayText(paymentAmount,3,(3*fontWidth-1),1)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("PAYMENT AMOUNT")
    g.displayText(string,2,0,1)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(paymentAmount,3,(3*fontWidth-1),1)

def state20():
    #vendor Screen
    g.clearDisplay(0)

    string = ("{:.^%d}" % lineLength).format("WAITING FOR FINGER")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)

    string = ("{:.^%d}" % lineLength).format("PLACE UR FINGER")
    g.displayText(string,3,0,1)




def state30():
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("SCANNING USER'S")
    g.displayText(string,2,0,0)
    string = ("{:.^%d}" % lineLength).format("FINGER NOW")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("SCANNING YOUR")
    g.displayText(string,2,0,1)
    string = ("{:.^%d}" % lineLength).format("FINGER NOW")
    g.displayText(string,3,0,1)

def state31():
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,3,0,1)

def state32():
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("NO ENOUGH BALANCE")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("NO ENOUGH BALANCE")
    g.displayText(string,3,0,1)





def state40(paymentAmount):
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("PAYMENT SUCCESSFUL")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)
    g.displayText(paymentAmount,3,(3*fontWidth-1),0)


    #user Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("PAYMENT SUCCESSFUL")
    g.displayText(string,2,0,1)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(paymentAmount,3,(3*fontWidth-1),1)


