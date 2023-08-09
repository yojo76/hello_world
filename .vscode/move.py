import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        px, py = pyautogui.position()
        time.sleep(60)
        px1, py1 = pyautogui.position()
        if px == px1 and py == py1:
            x+=1
            print("Movement not detected, increment counter at {}".format(datetime.now().time())) 
        else: 
            print("Movement detected, reset counter at {}".format(datetime.now().time()))
            x=0
    for i in range(0,20):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))