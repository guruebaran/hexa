__author__ = 'guru'
#state 10 = recharge amount
#state 20 = Ask's user to place their finger on FPS
#state 30 = Scanning ur finger now
#state 31 = account not found
#state 40 = recharge successful

#screen = 0 vendor,screen = 1 customer.

import GLCD as g

currentState = 0
fontWidth = 6
lineLength = 21


def state10(rechargeAmount = "0"):
    global currentState
    currentState = 10
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:^%d}" % lineLength).format("Recharge Amount")
    g.displayText(string,2,0,0)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("Recharge Amount")
    g.displayText(string,2,0,1)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)

def state20(amount = "0"):
    global currentState
    currentState = 20
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:^%d}" % lineLength).format("Recharging...")
    g.displayText(string,0,0,0)
    string = ("{:<%d}" % lineLength).format("Recharge Rs. ")
    g.displayText(string, 2, 0, 0)
    g.displayText(amount + " ?", 2, (13 * fontWidth - 1), 0)
    string = ("{:<%d}" % lineLength).format("Waiting for Finger")
    g.displayText(string,4,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("Recharging...")
    g.displayText(string,0,0,1)
    string = ("{:^%d}" % lineLength).format("Recharge Rs. ")
    g.displayText(string, 2, 0, 1)
    g.displayText(amount + " ?", 2, (13 * fontWidth - 1), 1)
    string = ("{:^%d}" % lineLength).format("Place ur Finger")
    g.displayText(string,4,0,1)




def state30():
    global currentState
    currentState = 30
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

def state31():
    global currentState
    currentState = 31
    #vendor Screen
    g.clearDisplay(0)
    g.clearDisplay()
    string = ("{:^%d}" % lineLength).format("Account Not Found")
    g.displayText(string,2,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("OOPS!")
    g.displayText(string, 2, 0, 1)
    string = ("{:^%d}" % lineLength).format("Account Not Found")
    g.displayText(string,3,0,1)





def state40(rechargeAmount,newBalance):
    global currentState
    currentState = 40
    #vendor Screen
    g.clearDisplay(0)
    string = ("{:^%d}" % lineLength).format("Recharge Successful")
    g.displayText(string,2,0,0)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,0)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),0)
    string = ("{:^%d}" % lineLength).format("Current Balance is")
    g.displayText(string,4,0,0)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,5,0,0)
    g.displayText(newBalance,5,(3*fontWidth-1),0)

    #user Screen
    g.clearDisplay(1)
    string = ("{:^%d}" % lineLength).format("Recharge Successful")
    g.displayText(string,2,0,1)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,3,0,1)
    g.displayText(rechargeAmount,3,(3*fontWidth-1),1)
    string = ("{:^%d}" % lineLength).format("Your Current Balance")
    g.displayText(string,4,0,0)
    string = ("{:<%d}" % lineLength).format("Rs.")
    g.displayText(string,5,0,0)
    g.displayText(newBalance,5,(3*fontWidth-1),0)

