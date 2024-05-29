import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()


finally:
    time.sleep(15)
    browser.quit()