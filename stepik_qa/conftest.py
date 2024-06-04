import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    # time.sleep(15)
    browser.quit()