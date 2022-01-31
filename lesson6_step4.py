from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)

try:
    
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()
    input1 = browser.find_element_by_id("input_value").text
    input2 = browser.find_element_by_id("answer")
    input1 = str(calc(str(input1)))
    input2.send_keys(input1) 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button2 = browser.find_element_by_id("solve")
    button2.click()




 # Отправляем заполненную форму
    #button2 = browser.find_element_by_css_selector("button.btn")
    #button2.click()
    #time.sleep(3)
    confirm_success = browser.switch_to.alert
    alert_text = confirm_success.text
    print(alert_text)    
    confirm_success.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
    

# не забываем оставить пустую строку в конце файла