import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# def calc(x):
#     x = int(x)
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# url = 'http://suninjuly.github.io/explicit_wait2.html'
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     WebDriverWait(driver, 12).until(
#         EC.text_to_be_present_in_element((By.ID, 'price'),'$100')
#     )
#     driver.find_element(By.ID, 'book').click()
#     x_el = driver.find_element(By.ID, 'input_value').text
#     driver.find_element(By.ID, 'answer').send_keys(calc(x_el))
#     driver.find_element(By.ID, 'solve').click()
#     time.sleep(7)
