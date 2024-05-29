import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log( abs(12 * math.sin(int(x))) ))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    var = browser.find_element(By.ID, 'input_value')
    var = var.text

    result = calc(var)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    chk = browser.find_element(By.ID, 'robotCheckbox')
    chk.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()


    btn = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()



finally:
    time.sleep(15)
    browser.quit()