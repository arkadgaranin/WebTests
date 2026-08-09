import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.NewsPage import NewsPageHelper, NewsPageLocators
from pages.UserProfilePage import UserProfilePageHelper

BASE_URL = 'https://sn.rv-school.ru/'
LOGIN = 'arkgaranin'
PASSWORD = 'amigo2690'


@allure.suite('Проверка ленты новостей')
@allure.title('Проверка скролла ленты новостей к определенной новости и вход в профиль ее автора')
def test_scroll_news_feed_and_enter_to_author_profile(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_username(LOGIN)
    LoginPage.enter_password(PASSWORD)
    LoginPage.click_login()
    NewsPage = NewsPageHelper(browser)
    NewsPage.scroll_to_item(NewsPageLocators.NEWS_ITEM_NUMBER_11)
    UserProfilePageHelper(browser)
