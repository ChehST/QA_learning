from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)
    

    btn = browser.find_element(By.ID, "button")


finally:
    browser.quit()