import os
import kbh

kb = kbh.KBHit()
print ('Enter a choice: \n1.Register\n2.search \n3.empty \nEsc to Exit ')
while 1:
    if kb.kbhit():
        x = kb.getch()
        if ord(x) == 27:
            print('hi')
            break
        else:
            print(x)