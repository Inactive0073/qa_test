import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

class TestAbs(unittest.TestCase):
    # 1.6

    def test_form_1(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            ...
            browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Name')
            browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Email')
            browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('Phone')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEquals(welcome_text, "Congratulations! You have successfully registered!", \
                              '[Error], values must be equal')
            time.sleep(10)

    def test_form_2(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            ...
            browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Name')
            browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Email')
            browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('Phone')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEquals(welcome_text, "Congratulations! You have successfully registered!", \
                              '[Error], values must be equal')
            time.sleep(10)


if __name__ == "__main__":
    unittest.main()
