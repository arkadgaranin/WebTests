from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    LOGIN_TAB = (By.ID, 'tabLogin')
    QR_TAB = (By.ID, 'tabQr')
    LOGIN_FIELD = (By.XPATH, '//input[@data-test-id="login-phone-email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-test-id="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="login-submit-btn"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@data-test-id="forgot-password-link"]')
    ERROR_TEXT = (By.XPATH, '//div[@data-test-id="login-error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()  # вызов функции чек-пейдж прописан здесь в конструкторе класса  для того, чтобы когда
        # в тесте создадим объект класса LoginPageHelper, то автомато вызвалась функция и проверила наличие элементов стр-цы

    def chek_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Нажимаем на кнопку Войти')
    def click_login(self):
        self.attach_screenschot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Вводим логин')
    def enter_username(self):
        self.attach_screenschot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys('arkgaranin')

    @allure.step('Вводим пароль')
    def enter_password(self):
        self.attach_screenschot()
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys('amigo2690')

    @allure.step('Проверяем текст ошибки')
    def get_error_text(self):
        self.attach_screenschot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
