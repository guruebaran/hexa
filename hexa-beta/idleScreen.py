__author__ = 'guru'
import GLCD as g

fontWidth = 6
lineLength = 21
currentState = 0

def state10():
    global currentState
    currentState = 10
    #vendor Screen
    g.clearDisplay(0)

    string = ("{:.^%d}" % lineLength).format("Project Hexa")
    g.displayText(string, 3, 0, 0)
    string = ("{:.^%d}" % lineLength).format("Welcomes You!!")
    g.displayText(string, 4, 0, 0)


    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("Project Hexa")
    g.displayText(string, 3, 0, 1)
    string = ("{:.^%d}" % lineLength).format("Welcomes You!!")
    g.displayText(string, 4, 0, 1)



