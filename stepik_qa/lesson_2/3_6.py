import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log( abs(12 * math.sin(int(x))) ))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    entry = browser.find_element(By.TAG_NAME,'button')
    entry.click()

    # get second page
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x = browser.find_element(By.ID,'input_value')
    x = x.text
    res = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)


    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()




finally:
    time.sleep(15)
    browser.quit()