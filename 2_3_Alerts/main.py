import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math



def calc(x):
    x = int(x)
    return str(math.log(abs(12 * math.sin(int(x)))))

# url = 'http://suninjuly.github.io/alert_accept.html'

# with webdriver.Chrome() as driver:
#     driver.get(url)
#     driver.find_element(By.TAG_NAME, 'button').click()
#     confirm = driver.switch_to.alert
#     confirm.accept()
#     x_el = driver.find_element(By.ID, 'input_value').text
#     driver.find_element(By.ID, 'answer').send_keys(calc(x_el))
#     driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#     time.sleep(7)


# url = 'https://suninjuly.github.io/redirect_accept.html'
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     driver.find_element(By.CLASS_NAME, 'trollface').click()
#     driver.switch_to.window(driver.window_handles[1]) # Открыли новое окно и перешли в него.
#     x_el = driver.find_element(By.ID, 'input_value').text
#     driver.find_element(By.ID, 'answer').send_keys(calc(x_el))
#     driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#     time.sleep(7)