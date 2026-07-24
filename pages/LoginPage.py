from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')  # Можно найти по ID
    # или по атрибуту для QA data-test-id: PASSWORD_FIELD = (By.XPATH, '//input[@data-test-id="password-input"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Показать пароль"]]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="enter-action"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//button[contains(@label, "Войти по QR-коду")]')
    RESTORING_ACCESS_LINK = (By.XPATH, '//button[contains(@aria-label, "Не получается войти")]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Зарегистрироваться")]]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    ERROR_TEXT = (By.XPATH, '//*[contains(@class, "LoginForm-module__error___1xmAD")]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()  # вызов функции чек-пейдж прописан здесь в конструкторе класса  для того, чтобы когда
        # в тесте создадим объект класса LoginPageHelper, то автомато вызвалась функция и проверила наличие элементов стр-цы

    def chek_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.SHOW_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_BUTTON)
        self.find_element(LoginPageLocators.RESTORING_ACCESS_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def enter_username(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys('arkgar@yandex.ru')

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
