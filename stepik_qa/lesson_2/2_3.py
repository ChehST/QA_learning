import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID,'num1').text
    num2 = browser.find_element(By.ID,'num2').text
    calc = int(num1) + int(num2)
    print(num1,num2,calc)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(calc))

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()


finally:
    time.sleep(15)
    browser.quit()