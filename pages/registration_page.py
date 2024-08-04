import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.first_name_input = (By.ID, 'firstName')
        self.last_name_input = (By.ID, 'lastName')
        self.email_input = (By.ID, 'userEmail')
        self.gender_radio_male = (By.XPATH, "//label[@for='gender-radio-1']")
        self.mobile_number_input = (By.ID, 'userNumber')
        self.date_of_birth_input = (By.ID, 'dateOfBirthInput')
        self.subjects_input = (By.ID, 'subjectsInput')

        self.hobbies_sport = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
        # self.hobbies_sport = (By.ID, 'hobbies-checkbox-1')

        self.upload_picture_input = (By.ID, 'uploadPicture')
        self.current_address_input = (By.ID, 'currentAddress')
        self.state_dropdown = (By.XPATH, "//input[@id='react-select-3-input']")
        self.city_dropdown = (By.XPATH, "//input[@id='react-select-4-input']")
        self.submit_button = (By.ID, 'submit')

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def enter_first_name(self, first_name):
        """ Находит элемент на веб-странице по ID и вводит указанный текст в это поле
        с помощью Selenium WebDriver."""
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
        time.sleep(2)

    def enter_subjects(self, subjects):
        self.driver.find_element(*self.subjects_input).send_keys(subjects)
        time.sleep(2)

    def select_hobbies_sport(self):

        # driver.findElement(By.id("hobbies-checkbox-1")).click()
        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.ID, "hobbies-checkbox-1")).click().perform()
        #
        # time.sleep(2)
        checkbox_label = self.driver.find_element(*self.hobbies_sport)
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

    def upload_picture(self, file_path):
        self.driver.find_element(*self.upload_picture_input).send_keys(file_path)

    def enter_current_address(self, address):
        self.driver.find_element(*self.current_address_input).send_keys(address)

    def select_state(self, state):
        self.driver.find_element(*self.state_dropdown).send_keys(state)
        self.driver.find_element(*self.state_dropdown).send_keys(Keys.ENTER)
        time.sleep(2)

    def select_city(self, city):
        self.driver.find_element(*self.city_dropdown).send_keys(city)
        self.driver.find_element(*self.city_dropdown).send_keys(Keys.ENTER)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
        time.sleep(20)
