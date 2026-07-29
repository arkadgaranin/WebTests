from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
import allure

BASE_URL = 'https://sn.rv-school.ru/'
LOGIN = 'arkgaranin'
INVALID_PASSWORD = 'amigo'


@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_username(LOGIN)

    for i in range(3):
        LoginPage.enter_password(INVALID_PASSWORD)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
