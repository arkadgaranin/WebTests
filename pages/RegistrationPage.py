from pages.BasePage import BasePageHelper
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


class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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


class RegistrationByPhonePageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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
        return country_items[random_number].get_attribute('value')

    @allure.step('Вводим номер телефона')
    def enter_phone(self, number):
        self.find_element(RegistrationByPhonePageLocators.PHONE_FIELD).send_keys(number)
        self.attach_screenschot()

    @allure.step('Нажимаем на кнопку Получить код')
    def click_get_code_button(self):
        self.find_element(RegistrationByPhonePageLocators.SEND_CODE_BUTTON).click()
        self.attach_screenschot()


class EnteringCodeFromSmsPageLocators:
    SMS_CODE_FIELD = (By.XPATH, '//*[@data-test-id="sms-code-input"]')
    VERIFY_CODE_BTN = (By.XPATH, '//*[@data-test-id="phone-verify-code-btn"]')
    CHANGE_NUMBER_LINK = (By.XPATH, '//*[@data-test-id="phone-back-to-step-1"]')
    RETURN_LOGIN_LINK = (By.XPATH, '//*[@data-test-id="login-link-anchor"]')
    PHONE_NUMBER_TEXT = (By.XPATH, '//*[@data-test-id="phone-step-2-number"]')


class EnteringCodeFromSmsPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(EnteringCodeFromSmsPageLocators.SMS_CODE_FIELD)
            self.find_element(EnteringCodeFromSmsPageLocators.VERIFY_CODE_BTN)
            self.find_element(EnteringCodeFromSmsPageLocators.CHANGE_NUMBER_LINK)
            self.find_element(EnteringCodeFromSmsPageLocators.RETURN_LOGIN_LINK)
            self.find_element(EnteringCodeFromSmsPageLocators.PHONE_NUMBER_TEXT)

    def get_phone_number_text(self):
        return self.find_element(EnteringCodeFromSmsPageLocators.PHONE_NUMBER_TEXT).text
