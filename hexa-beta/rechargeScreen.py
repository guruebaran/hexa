__author__ = 'guru'
#state 10 = recharge amount
#state 20 = Ask's user to place their finger on FPS
#state 30 = Scanning ur finger now
#state 31 = account not found
#state 40 = recharge successful

#screen = 0 vendor,screen = 1 customer.

import GLCD as g

fontWidth = 6
lineLength = 21


def state10(rechargeAmount):
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("RECHARGE AMOUNT")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("RECHARGE AMOUNT")
    g.displayText(string,2,0,1)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)

def state20():
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("RECHARGING")c
    g.displayText(string,0,0,0)
    string = ("{:.^%d}" % lineLength).format("WAITING FOR FINGER")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("RECHARGING")c
    g.displayText(string,0,0,1)
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
    g.clearDisplay()
    string = ("{:.^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,2,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("ACCOUNT NOT FOUND")
    g.displayText(string,2,0,1)





def state40(rechargeAmount,newBalance):
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:.^%d}" % lineLength).format("RECHARGE SUCCESSFUL")
    g.displayText(string,2,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),0)
    string = ("{:.^%d}" % lineLength).format("YOUR NEW BALANCE IS")
    g.displayText(string,4,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,5,0,0)
    g.displayText(newBalance,5,(3*fontWidth-1),0)

    #user Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("RECHARGE SUCCESSFUL")
    g.displayText(string,2,0,1)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)
    string = ("{:.^%d}" % lineLength).format("YOUR NEW BALANCE IS")
    g.displayText(string,4,0,0)
    string = ("{:.<%d}" % lineLength).format("Rs.")
    g.displayText(string,5,0,0)
    g.displayText(newBalance,5,(3*fontWidth-1),0)

