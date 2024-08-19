import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# url = 'https://suninjuly.github.io/simple_form_find_task.html'

# 1.2
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(By.NAME, 'first_name').send_keys('Name')
#     browser.find_element(By.NAME, 'last_name').send_keys('Surname')
#     browser.find_element(By.CLASS_NAME, 'city').send_keys('City')
#     browser.find_element(By.ID, 'country').send_keys('Country')
#     browser.find_element(By.ID, 'submit_button').click()
#     time.sleep(10)

# 1.3
# url = 'http://suninjuly.github.io/find_link_text'
# val = '224592'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(By.LINK_TEXT, val).click()
#     browser.find_element(By.NAME, 'first_name').send_keys('Name')
#     browser.find_element(By.NAME, 'last_name').send_keys('Surname')
#     browser.find_element(By.CLASS_NAME, 'city').send_keys('City')
#     browser.find_element(By.ID, 'country').send_keys('Country')
#     browser.find_element(By.CLASS_NAME, 'btn-default').click()
#     time.sleep(10)

# 1.4
# url = 'http://suninjuly.github.io/huge_form.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     elms = browser.find_elements(By.TAG_NAME, 'input')
#     for el in elms:
#         el.send_keys('Answer')
#     browser.find_element(By.CLASS_NAME, 'btn-default').click()
#     time.sleep(10)

# 1.5
# url = 'http://suninjuly.github.io/find_xpath_form'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(By.NAME, 'first_name').send_keys('Name')
#     browser.find_element(By.NAME, 'last_name').send_keys('Surname')
#     browser.find_element(By.CLASS_NAME, 'city').send_keys('City')
#     browser.find_element(By.ID, 'country').send_keys('Country')
#     browser.find_element(By.XPATH, '//button[@type="submit"]').click()
#     time.sleep(10)

# 1.6
with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    browser.find_element(By.NAME, 'first_name').send_keys('Name')
    browser.find_element(By.NAME, 'last_name').send_keys('Surname')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('City')
    browser.find_element(By.ID, 'country').send_keys('Country')

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
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)