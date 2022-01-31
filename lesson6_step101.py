from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # browser = webdriver.Chrome() это для стандартных настроек webdriver
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR,
                         '[placeholder="Input your first name"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR,
                         '[placeholder="Input your last name"]').send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys("test@email.ru")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys("12345678")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys("My Address")

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

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
