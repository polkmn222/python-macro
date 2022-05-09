"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver")

driver.get("www.google.com")
driver.implicitly_wait(3)
"""
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url='https://www.google.com/')

search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search_box.send_keys('greeksharifa.github.io')
search_box.send_keys(Keys.RETURN)

elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a/h3/span')

for element in elements:
    print(element.text)
    print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

sleep(3)
driver.close()
"""
"""
import pyautogui
import time
while 1:
    pyautogui.click(x=600,y=400)
    time.sleep(0.1)
    pyautogui.doubleClick(x=650,y=450)
    time.sleep(0.1)
"""

"""
while 1:
    pyautogui.press('f5', interval=3)
    print('Do it')
    pyautogui.click(x=600,y=400, interval=1)
    pyautogui.click(x=700,y=300, interval=1)
    pyautogui.click(x=800,y=500, interval=1)
    if keyboard.is_pressed('f12'):
        break
"""
"""
position = pyautogui.position()
if keyboard.is_pressed('enter'):
    print(position)
    time.sleep(0.2)
"""
"""
pyautogui.click(x=50,y=500, interval=1)
pyautogui.click(x=60,y=950, interval=1)

"""
"""
while True:
    set = 'qwertyuiopasdfghjklzxcvbnm1234567890A.!'
    paw = ''
    pyautogui.doubleClick(x=50,y=500, interval=0.1)
    for i in range(1,6):
        if i==2: continue
        paw += random.choice(set)
        pyautogui.typewrite(paw, interval=0.001)
       
    pyautogui.click(x=60,y=950, interval=1)

"""

import pyautogui
import keyboard
import time
import random

# pip install pyautogui
# pip install keyboard

while True:
    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(6):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break

    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(7):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break

    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(8):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break

    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(9):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break

    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(10):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break

    while True:
        set = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        set1 = 'AQ'
        set2 = '.!'
        paw = []

        pyautogui.doubleClick(x=60,y=505, interval=0.1)
        paw += random.choice(set1)
        paw += random.choice(set2)

        for i in range(11):
            paw += random.choice(set)

        random.shuffle(paw)    
        print(paw)
        pyautogui.typewrite(paw, interval=0.001)
        pyautogui.click(x=60,y=950, interval=1)
        break
    

    if keyboard.is_pressed('F6'):
        break


