from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper
from pages.LoginPage import LoginOkPageHelper
import allure

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    LoginOkPageHelper(browser)
    current_window_id = BasePage.get_windows_id(0)
    BasePage.click_vk_ecosystem()
    BasePage.click_more_button()
    new_window_id = BasePage.get_windows_id(1)
    BasePage.switch_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.switch_window(current_window_id)
    LoginOkPageHelper(browser)
