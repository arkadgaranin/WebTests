from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password') # Можно найти по ID
    # или по атрибуту для QA data-test-id: PASSWORD_FIELD = (By.XPATH, '//input[@data-test-id="password-input"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Показать пароль"]]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="enter-action"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//button[contains(@label, "QR")]')
    RESTORING_ACCESS_LINK = (By.XPATH, '//button[contains(@aria-label, "Не получается войти")]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Зарегистрироваться")]]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')

class LoginPageHelper(BasePage):
    pass
