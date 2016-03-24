__author__ = 'guru'
import RPi.GPIO as GPIO
from time import sleep



#define ConfigureLCDPINsDirection(Value)    (TRISD = Value,             \
#                                             TRISCbits.TRISC3 = Value,  \
#                                             TRISCbits.TRISC4 = Value,  \
 #                                            TRISCbits.TRISC5 = Value,  \
  #                                           TRISCbits.TRISC6 = Value,  \
   #                                          TRISCbits.TRISC7 = Value)



Enable = 1
Disable = 0

Command = 0
Data = 1

LeftChip = 1
RightChip = 2
BothChip = 3

DisplayON = 63
DisplayStartLine = 192

ColourON = 1
ColourOFF = 0

Index0 = 0x40
Index1 = 0x50
Index2 = 0x60
Index3 = 0x70
Index4 = 0x80
Index5 = 0x90
Index6 = 0xA0
Index7 = 0xB0

Page0 = 0xB8
Page1 = 0xB9
Page2 = 0xBA
Page3 = 0xBB
Page4 = 0xBC
Page5 = 0xBD
Page6 = 0xBE
Page7 = 0xBF


DataBusLCD = [5,6,13,19,26,12,16,20] #D0 to D7
EnableLCD = 21
RegisterSelect = 25
ChipSelect1 = 24
ChipSelect2 = 23
ResetLCD = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RegisterSelect, GPIO.OUT)
GPIO.setup(EnableLCD, GPIO.OUT)
GPIO.setup(ChipSelect1, GPIO.OUT)
GPIO.setup(ChipSelect2, GPIO.OUT)
GPIO.setup(ResetLCD, GPIO.OUT)
for Pin in DataBusLCD:
    GPIO.setup(Pin, GPIO.OUT)

def DataBusLCDfn(data):
    DataString = "{:0>8}".format("{0:b}".format(data))
    for i in range(8):
        GPIO.output(DataBusLCD[i],int(DataString[i]))

def InitializeGraphicalLCD():
    GPIO.output(RegisterSelect,Command)
    GPIO.output(EnableLCD,Enable)
    DataBusLCDfn(Disable)
    GPIO.output(ChipSelect1 , Disable)
    GPIO.output(ChipSelect2 , Disable)
    GPIO.output(ResetLCD , Enable)
    sleep(0.00001)

    GPIO.output(ResetLCD , Disable)                                 # Normal Operation
    WriteCommandToLCD(DisplayON, BothChip)           #  Sending 63 to both chip CS1 and CS2
    WriteCommandToLCD(DisplayStartLine, BothChip)      #  Sending 192 to both chip CS1 and CS2
    ClearScreen()


def ChipSelection(Chip):
    if(Chip == 1):
        GPIO.output(ChipSelect1 , Enable)
        GPIO.output(ChipSelect2 , Disable)
    elif(Chip == 2):
        GPIO.output(ChipSelect1 , Disable)
        GPIO.output(ChipSelect2 , Enable)
    else:
        GPIO.output(ChipSelect1 , Enable)
        GPIO.output(ChipSelect2 , Enable)


def ToggleEnablePin():
    sleep(0.000001)
    GPIO.output(EnableLCD , Enable)
    sleep(0.000001)
    GPIO.output(EnableLCD , Disable)


def WriteCommandToLCD(CommandToLCD,SelectChip):
    # sending data to LCD.
    ChipSelection(SelectChip)
    GPIO.output(RegisterSelect , Command)
    DataBusLCDfn(CommandToLCD)
    ToggleEnablePin()


def WriteDataToLCD(DataToLCD,SelectChip):
    # sending data to LCD.
    ChipSelection(SelectChip)
    GPIO.output(RegisterSelect , Data)
    DataBusLCDfn(DataToLCD)
    ToggleEnablePin()


def WriteAddressToLCD(AddressX,AddressY,SelectChip):
    # sending X address.
    WriteCommandToLCD(AddressX, SelectChip)
   # sending Y address.
    WriteCommandToLCD(AddressY, SelectChip)


def ClearScreen():
    X = 0
    Page = Page0
    while(X<8):
        X+=1
        WriteAddressToLCD(Page, Index0, BothChip)
        Page+=1
        Y=0
        while(Y<64):
            Y+=1
            WriteDataToLCD(0x00, BothChip)


def FillScreen():
    X = 0
    Page = Page0
    while(X<8):
        X+=1
        WriteAddressToLCD(Page, Index0, BothChip)
        Page+=1
        Y=0
        while(Y<64):
            Y+=1
            WriteDataToLCD(0xF0, BothChip)


def DisplayPicture(PtrArray):
    X = 0
    Page = Page0
    while(X<8):
        X+=1
        WriteAddressToLCD(Page, Index0, LeftChip)
        Y=0
        while(Y<64):
            WriteDataToLCD(PtrArray, LeftChip)
            Y+=1
        WriteAddressToLCD(Page, Index0, RightChip)
        Y=0
        while(Y<64):
            WriteDataToLCD(PtrArray, RightChip)
            Y+=1

InitializeGraphicalLCD()
FillScreen()
#ClearScreen()
GPIO.cleanup()