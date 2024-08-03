import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def allure_logging(setup, request):
    yield
    if request.node.rep_call.failed:
        setup.save_screenshot("screenshot.png")
        allure.attach.file("screenshot.png", attachment_type=AttachmentType.PNG)


def pytest_exception_interact(node, call, report):
    driver = node.funcargs['setup']  # Получаем driver из параметра setup фикстуры
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
