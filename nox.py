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
import pyautogui
import keyboard
import time
import random

# pip install pyautogui
# pip install keyboard
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
while True:
    set = 'qwertyuiopasdfghjklzxcvbnm1234567890A'
    paw = ''
    pyautogui.doubleClick(x=40,y=365, interval=0.1)
    for i in range(1,5):
        paw += random.choice(set)
        pyautogui.typewrite(paw, interval=0.001)
       
    pyautogui.click(x=100,y=660, interval=1)
