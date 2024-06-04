import time
import math

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secret import *



@pytest.mark.parametrize('link',['https://stepik.org/lesson/236895/step/1',
                                 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1',
                                 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1',
                                 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1',
                                 'https://stepik.org/lesson/236905/step/1',
                                ]
)
class TestInoplanet():
    
    def test_login_and_comment(self,browser,link):
        browser.get(link)
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

        time.sleep(5)

        # find textarea with answer
        textarea = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        btn_submit = browser.find_element(By.CSS_SELECTOR,'button.submit-submission')
        answer = math.log(int(time.time()))
        textarea.send_keys(answer)
        btn_submit.click()

        result = browser.find_element(By.CSS_SELECTOR, '#ember522 p')
        result = text.text

        assert result == 'correct!'
