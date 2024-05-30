import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLesson1(unittest.TestCase):
    def test_reg1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            req1 = browser.find_element(By.CSS_SELECTOR,'.first_block .first_class input')
            req1.send_keys('rand')

            req2 = browser.find_element(By.CSS_SELECTOR,'.first_block .second_class input')
            req2.send_keys('rand2')

            req3 = browser.find_element(By.CSS_SELECTOR,'.first_block .third_class input')
            req3.send_keys('rand3')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Shuld be grats text")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


        
        
    def test_reg2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            req1 = browser.find_element(By.CSS_SELECTOR,'.first_block .first_class input')
            req1.send_keys('rand')

            req2 = browser.find_element(By.CSS_SELECTOR,'.first_block .second_class input')
            req2.send_keys('rand2')

            req3 = browser.find_element(By.CSS_SELECTOR,'.first_block .third_class input')
            req3.send_keys('rand3')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Shuld be grats text")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

        
if __name__ == "__main__":
    unittest.main()