from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class UserProfilePageLocators:
    SUBSCRIBE_BUTTON = (By.XPATH, '//*[@data-test-id="btn-follow"]')
    POSTS_TITLE = (By.XPATH, '//h2[text()="Записи"]')


class UserProfilePageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(UserProfilePageLocators.SUBSCRIBE_BUTTON)
            self.find_element(UserProfilePageLocators.POSTS_TITLE)
