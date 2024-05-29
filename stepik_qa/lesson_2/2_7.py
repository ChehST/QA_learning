import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/file_input.html'

curent_dir = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(curent_dir,'payload.txt')

print(file)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME,'firstname')
    name.send_keys('rand')

    lastname = browser.find_element(By.NAME,'lastname')
    lastname.send_keys('rand')

    email = browser.find_element(By.NAME,'email')
    email.send_keys('rand')

    attacment = browser.find_element(By.CSS_SELECTOR,'input#file')
    attacment.send_keys(file)

    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()




finally:
    time.sleep(15)
    browser.quit()