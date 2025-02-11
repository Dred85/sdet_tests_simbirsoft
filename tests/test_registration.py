import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from config import picture_path
import allure


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "first_name, last_name, email, gender, mobile_number, dob, subjects, picture_path, address, state, city",
    [("Александр", "Олонов", "adrolv@rambler.ru", "Male", "9101268340", "01-01-1990", "Maths",
      picture_path,
      # "/home/dred/PycharmProjects/sdet_test_simbirsoft/images/electron.jpg",
      "улица Горная", "NCR", "Delhi")])
def test_fill_registration_form(setup, first_name, last_name, email, gender, mobile_number, dob, subjects, picture_path,
                                address, state, city):
    driver = setup
    registration_page = RegistrationPage(driver)
    registration_page.open_page()

    registration_page.enter_first_name(first_name)
    registration_page.enter_last_name(last_name)
    registration_page.enter_email(email)
    registration_page.select_gender()
    registration_page.enter_mobile_number(mobile_number)
    registration_page.enter_date_of_birth(dob)
    registration_page.enter_subjects(subjects)
    registration_page.select_hobbies_sport()
    registration_page.upload_picture(picture_path)
    registration_page.enter_current_address(address)
    registration_page.select_state(state)
    registration_page.select_city(city)

    registration_page.submit_form()

    # Формирование отчета Allure
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
