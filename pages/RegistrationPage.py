from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, '//*[@data-test-id="display-name"]')
    LOGIN_FIELD = (By.XPATH, '//*[@data-test-id="username"]')
    EMAIL_FIELD = (By.XPATH, '//*[@data-test-id="email"]')
    PHONE_FIELD = (By.XPATH, '//*[@data-test-id="phone"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@data-test-id="register-password"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//*[@data-test-id="confirm-password"]')
    CREATE_ACCOUNT_BTN = (By.XPATH, '//*[@data-test-id="register-submit-btn"]')
    REGISTRATION_BY_PHONE_BUTTON = (By.XPATH, '//*[@data-test-id="register-phone-toggle"]')
    RETURN_LOGIN_LINK = (By.XPATH, '//*[@data-test-id="login-link-anchor"]')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(RegistrationPageLocators.NAME_FIELD)
            self.find_element(RegistrationPageLocators.LOGIN_FIELD)
            self.find_element(RegistrationPageLocators.EMAIL_FIELD)
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.PASSWORD_FIELD)
            self.find_element(RegistrationPageLocators.CONFIRM_PASSWORD_FIELD)
            self.find_element(RegistrationPageLocators.CREATE_ACCOUNT_BTN)
            self.find_element(RegistrationPageLocators.REGISTRATION_BY_PHONE_BUTTON)
            self.find_element(RegistrationPageLocators.RETURN_LOGIN_LINK)

    @allure.step('Переходим в регистрацию по телефону')
    def click_registration_by_phone(self):
        self.attach_screenschot()
        self.find_element(RegistrationPageLocators.REGISTRATION_BY_PHONE_BUTTON).click()


class RegistrationByPhonePageLocators:
    COUNTRY_CODE_LIST = (By.XPATH, '//*[@data-test-id="phone-country-select"]')
    COUNTRY_CODE_ITEM = (By.XPATH, '//option[starts-with(@data-test-id, "phone-country-option")]')
    PHONE_FIELD = (By.XPATH, '//*[@data-test-id="phone-number-input"]')
    SEND_CODE_BUTTON = (By.XPATH, '//*[@data-test-id="phone-send-code-btn"]')
    RETURN_REGISTR_BY_EMAIL_LINK = (By.XPATH, '//*[@data-test-id="phone-cancel-btn"]')
    RETURN_LOGIN_LINK = (By.XPATH, '//*[@data-test-id="login-link-anchor"]')


class RegistrationByPhonePageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(RegistrationByPhonePageLocators.COUNTRY_CODE_LIST)
            self.find_element(RegistrationByPhonePageLocators.PHONE_FIELD)
            self.find_element(RegistrationByPhonePageLocators.SEND_CODE_BUTTON)
            self.find_element(RegistrationByPhonePageLocators.RETURN_REGISTR_BY_EMAIL_LINK)
            self.find_element(RegistrationByPhonePageLocators.RETURN_LOGIN_LINK)

    @allure.step('Выбираем рандомную страну с ее кодом')
    def select_random_country_and_code(self):
        random_number = random.randint(0, 39)
        country_items = self.find_elements(RegistrationByPhonePageLocators.COUNTRY_CODE_ITEM)
        country_items[random_number].click()
        self.attach_screenschot()
        return country_items[random_number].text

    @allure.step('Получаем значение атрибута value из поля "Код страны и номер"')
    def get_phone_value(self):
        return self.find_element(RegistrationByPhonePageLocators.COUNTRY_CODE_LIST).get_attribute('value')
