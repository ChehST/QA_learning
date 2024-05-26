import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    tarlink = browser.find_element(By.LINK_TEXT,'224592')
    tarlink.click()

    input_fn = browser.find_element(By.TAG_NAME, 'input')
    input_fn.send_keys('Sergey')

    input_ln = browser.find_element(By.NAME, 'last_name')
    input_ln.send_keys('ChaChaCha')

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Chelyaba')
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()