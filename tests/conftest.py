import pytest
from selenium import webdriver

#
# @pytest.fixture(scope="session")
# def setup():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()