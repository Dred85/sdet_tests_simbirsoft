import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains



def test_checkbox():
    driver = webdriver.Chrome()

    # Открытие страницы и максимизация окна
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()

    # Проверка и клик на чекбокс
    checkbox_label = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")

    # Проверка состояния чекбокса
    if not checkbox_label.is_selected():
        checkbox_label.click()

    # Проверка, виден ли чекбокс
    if checkbox_label.is_displayed():
        checkbox_label.click()

    # Проверка, доступен ли чекбокс
    if checkbox_label.is_enabled():
        checkbox_label.click()


    time.sleep(5)

    # Закрытие браузера
    driver.quit()



