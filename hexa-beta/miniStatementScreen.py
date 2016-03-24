__author__ = 'guru'

#state 10 = Ask's user to place their finger on FPS
#state 20 = Scanning ur finger now
#state 21 = Acccount not found
#state 30 = Mini Statement(last 3 transcations)


#screen = 0 vendor,screen = 1 customer.

import GLCD as g

fontWidth = 6
lineLength = 21


def state10():
    #vendor Screen
    g.clearDisplay(0)

    string = ("{:.^%d}" % lineLength).format("WAITING FOR FINGER")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("PLACE UR FINGER")
    g.displayText(string,3,0,1)




def state20():
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


def state21():
    #vendor Screen

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,2,0,1)



def state30(date,transcationPoint,plusMinus,amount,phoneNumber):
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("MINI-STATEMENT")
    g.displayText(string,0,0,0)
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,1,0,0)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,1,(6*fontWidth-1),0)
    string = ("{:.^%d}" % lineLength).format(" DATE    VNU P/R  AMT")
    g.displayText(string,2,0,0)
    string = "{:<8}".format(date)
    g.displayText(string,3,0,0)
    string = "{:<3}".format(transcationPoint)
    g.displayText(string,3,9,0)
    string = "{:<1}".format(plusMinus)
    g.displayText(string,3,13,0)
    string = "{:<4}".format(amount)
    g.displayText(string,3,17,0)

    #user Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("MINI-STATEMENT")
    g.displayText(string,0,0,1)
    string = ("{:.<%d}" % lineLength).format("PH.NO:")
    g.displayText(string,1,0,1)
    string = "{:<10}".format(phoneNumber)
    g.displayText(string,1,(6*fontWidth-1),0)
    string = ("{:.^%d}" % lineLength).format(" DATE    VNU P/R  AMT")
    g.displayText(string,2,0,1)
    string = "{:<8}".format(date)
    g.displayText(string,3,0,1)
    string = "{:<3}".format(transcationPoint)
    g.displayText(string,3,9,1)
    string = "{:<1}".format(plusMinus)
    g.displayText(string,3,13,1)
    string = "{:<4}".format(amount)
    g.displayText(string,3,17,1)


