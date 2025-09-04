from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def func(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button1 = browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text

    func = str(func(int(x)))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(func)

    button2 = browser.find_element(By.ID, 'solve').click()



finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()