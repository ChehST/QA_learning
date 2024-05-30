import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = 'https://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log( abs(12 * math.sin(int(x))) ))


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
try:
        btn = browser.find_element(By.TAG_NAME,'button')
        price = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
        btn.click()

        x = browser.find_element(By.ID,'input_value')
        x = x.text
        res = calc(x)

        answer = browser.find_element(By.ID, 'answer')
        answer.send_keys(res)

        solve = browser.find_element(By.ID,'solve')
        solve.click()

finally:
        time.sleep(15)
        browser.quit()