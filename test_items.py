import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



def test_language_changing(browser):

    browser.get("https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/")

    assert WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary'))), 'Кнопка добавления в корзину не найдена'

    time.sleep(30)







