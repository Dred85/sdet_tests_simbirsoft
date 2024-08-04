import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains



def test_checkbox():
    driver = webdriver.Chrome()

    # Открытие страницы и максимизация окна
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()

    driver.find_element().send_keys(file_path)




