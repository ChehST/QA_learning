import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log( abs(12 * math.sin(int(x))) ))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    res = calc(x)
    
    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(res)

    chk = browser.find_element(By.ID, 'robotCheckbox')
    chk.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    time.sleep(10)

finally:
    browser.quit()
