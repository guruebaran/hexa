__author__ = 'guru'
import GLCD as g

fontWidth = 6
lineLength = 21


def state10():
    #vendor Screen
    g.clearDisplay(0)

    string = ("{:.^%d}" % lineLength).format("WELCOME")
    g.displayText(string,3,0,0)

    #User Screen
    g.clearDisplay(1)
    string = ("{:.^%d}" % lineLength).format("WELCOME")
    g.displayText(string,3,0,1)



