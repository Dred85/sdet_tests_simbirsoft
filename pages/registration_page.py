from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.first_name_input = (By.ID, 'firstName')
        self.last_name_input = (By.ID, 'lastName')
        self.email_input = (By.ID, 'userEmail')
        self.gender_radio_male = (By.ID, 'gender-radio-1')
        self.mobile_number_input = (By.ID, 'userNumber')
        self.date_of_birth_input = (By.ID, 'dateOfBirthInput')
        self.subjects_input = (By.ID, 'subjectsInput')
        self.upload_picture_input = (By.ID, 'uploadPicture')
        self.current_address_input = (By.ID, 'currentAddress')
        self.state_dropdown = (By.ID, 'state')
        self.city_dropdown = (By.ID, 'city')
        self.submit_button = (By.ID, 'submit')

    def open_page(self):
        self.driver.get(self.url)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def select_gender(self):
        self.driver.find_element(*self.gender_radio_male).click()

    def enter_mobile_number(self, mobile_number):
        self.driver.find_element(*self.mobile_number_input).send_keys(mobile_number)

    def enter_date_of_birth(self, dob):
        self.driver.find_element(*self.date_of_birth_input).send_keys(dob)

    def enter_subjects(self, subjects):
        self.driver.find_element(*self.subjects_input).send_keys(subjects)

    def upload_picture(self, file_path):
        self.driver.find_element(*self.upload_picture_input).send_keys(file_path)

    def enter_current_address(self, address):
        self.driver.find_element(*self.current_address_input).send_keys(address)

    def select_state(self, state):
        state_dropdown = self.driver.find_element(*self.state_dropdown)
        state_dropdown.click()
        state_option = state_dropdown.find_element(By.XPATH, f".//option[text()='{state}']")
        state_option.click()

    def select_city(self, city):
        city_dropdown = self.driver.find_element(*self.city_dropdown)
        city_dropdown.click()
        city_option = city_dropdown.find_element(By.XPATH, f".//option[text()='{city}']")
        city_option.click()

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
