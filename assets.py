from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    op2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    op2.click()

    op1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    op1.click()

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    
    btn = browser.find_element(By.XPATH, "/html/body/div/form/button")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
