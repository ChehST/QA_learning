from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secret import *

link = 'https://stepik.org/lesson/236895/step/1'

def test_login_button(browser):
    
    login_btn =  WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a#ember459"))
    )
    login_btn.click()

    input_login = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#id_login_email"))
    )
    input_login.send_keys(EMAIL)

    input_pass = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#id_login_password"))
    )
    input_pass.send_keys(PASS)

    sign_btn = browser.find_element(By.CSS_SELECTOR,'button.sign-form__btn')
    sign_btn.click()
