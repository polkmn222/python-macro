import pyautogui
import keyboard
import time
import random

set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
set1 = 'AQ'
set2 = '.!'
paw = []


pyautogui.doubleClick(x=60,y=505, interval=0.1)

paw += random.choice(set1)
paw += random.choice(set2)
for i in range(6):
    paw += random.choice(set)
    #print(paw)    
    
random.shuffle(paw)       
print(paw)
pyautogui.typewrite(paw, interval=0.001)
pyautogui.click(x=60,y=950, interval=1)
