import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 2.1
# url = 'https://suninjuly.github.io/math.html'

# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     x_element = browser.find_element(By.CSS_SELECTOR, '[id=input_value]').text
#     browser.find_element(By.ID, 'robotCheckbox').click()
#     browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]').click()
#     browser.find_element(By.ID, 'answer').send_keys(calc(x_element))
#     browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#     time.sleep(5)

# 2.1.2
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# url = 'https://suninjuly.github.io/get_attribute.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     x_element = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
#     browser.find_element(By.ID, 'answer').send_keys(calc(x_element))
#     browser.find_element(By.ID, 'robotCheckbox').click()
#     browser.find_element(By.ID, 'robotsRule').click()
#     browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#     time.sleep(5)


# 2.2.1
# from selenium.webdriver.support.ui import Select
#
# url = 'http://suninjuly.github.io/selects1.html'
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     _sum = int(driver.find_element(By.ID, 'num1').text) + int(driver.find_element(By.ID, 'num2').text)
#     _select = Select(driver.find_element(By.ID, 'dropdown'))
#     _select.select_by_value(str(_sum))
#     driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#     time.sleep(7)


# 2.2.2
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# url = 'http://suninjuly.github.io/execute_script.html'
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     x = int(driver.find_element(By.ID, 'input_value').text)
#     driver.find_element(By.ID, 'answer').send_keys(calc(x))
#     driver.execute_script('window.scrollBy(0,100);')
#     for opt in ('robotCheckbox', 'robotsRule'):
#         driver.find_element(By.CSS_SELECTOR, f'[for={opt}]').click()
#     driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#     time.sleep(8)


# 2.2.3

import os

# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.abspath(__file__))

url = 'http://suninjuly.github.io/file_input.html'
_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'empty.txt')
with webdriver.Chrome() as driver:
    driver.get(url)
    driver.find_element(By.NAME, 'firstname').send_keys('Value')
    driver.find_element(By.NAME, 'lastname').send_keys('Value')
    driver.find_element(By.NAME, 'email').send_keys('Value')
    driver.find_element(By.ID, 'file').send_keys(_file)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    time.sleep(7)
