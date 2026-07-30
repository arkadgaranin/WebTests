from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, '//*[@data-test-id="recovery-phone-btn"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-test-id="recovery-email-btn"]')
    QR_CODE = (By.XPATH, '//*[@data-test-id="qr-image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-test-id="support-contact-btn"]')


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(RecoveryPageLocators.PHONE_BUTTON)
            self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
            self.find_element(RecoveryPageLocators.QR_CODE)
            self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
