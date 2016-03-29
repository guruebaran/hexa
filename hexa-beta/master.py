import RPi.GPIO as GPIO
import database
import fpsDriver
import idleScreen as idls
import miniStatementScreen as mins
import rechargeScreen as rchs
import userRegistrationScreen as regs
import kbh

state = 0
kb = kbh.KBHit()


GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # register
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # recharge
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # payment
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # mini
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # back


def registermode():
    global state
    state = 1

def rechargemode():
    global state
    state = 2

def paymentmode():
    global state
    state = 3

def miniStatementmode():
    global state
    state = 4


while True:
    if kb.kbhit():
        x = kb.getch()
        if state == 1:
            print("1")

        if state == 2:
            print("2")

        if state == 3:
            print("3")

        if state == 4:
            print("4")

    if GPIO.input(16) ==1:
        if state == 0:
            registermode()
    if GPIO.input(20) ==1:
        if state == 0:
            rechargemode()
    if GPIO.input(21) == 1:
        if state == 0:
            paymentmode()
    if GPIO.input(21) ==1:
        if state == 0:
            miniStatementmode()
        elif state == 3:

            print("payment mode")
        elif state == 2:

            print("recharge mode")
        elif state == 4:
            miniStatementmode()
        elif state == 1:
            print ("In register mode, Unexpected behavior")

#---------------------------------------------------------------------------------------------------------------------










GPIO.cleanup()