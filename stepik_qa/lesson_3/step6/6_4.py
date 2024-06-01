from selenium.webdriver.common.by import By

link = 'https://stepik.org/lesson/236895/step/1'

def test_login_button(browser):
    browser.get(link)
    browser.find_element(By.ID, "ember459")






