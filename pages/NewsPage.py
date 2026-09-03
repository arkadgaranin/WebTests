from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class NewsPageLocators:
    TITLE = (By.XPATH, '//*[@data-test-id="feed-title" and text()="Лента"]')
    FIELD_WHATS_NEW = (By.XPATH, '//*[@data-test-id="post-textarea"]')
    BUTTON_PUBLISH = (By.XPATH, '//*[@data-test-id="btn-post"]')
    TAB_NEWS = (By.XPATH, '//*[@data-test-id="link-feed" and text()="Новости"]')
    TAB_MY_PAGE = (By.XPATH, '//*[@data-test-id="link-profile" and text()="Моя страница"]')
    TAB_FRIENDS = (By.XPATH, '//*[@data-test-id="link-friends" and text()="Друзья"]')
    TAB_MESSAGES = (By.XPATH, '//*[@data-test-id="link-messages" and text()="Сообщения"]')
    NEWS_ITEM = (By.XPATH, '//article[starts-with(@data-test-id, "post-")]')
    NEWS_ITEM_NUMBER_11 = (By.XPATH, '//*[@data-test-id="post-header-3"]')


class NewsPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки стр-цы'):
            self.attach_screenschot()
            self.find_element(NewsPageLocators.TITLE)
            self.find_element(NewsPageLocators.FIELD_WHATS_NEW)
            self.find_element(NewsPageLocators.BUTTON_PUBLISH)
            self.find_element(NewsPageLocators.TAB_NEWS)
            self.find_element(NewsPageLocators.TAB_MY_PAGE)
            self.find_element(NewsPageLocators.TAB_FRIENDS)
            self.find_element(NewsPageLocators.TAB_MESSAGES)
            self.find_element(NewsPageLocators.NEWS_ITEM)

    @allure.step('Скролл к определенной новости и вход в профиль ее автора')
    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
        self.attach_screenschot()
