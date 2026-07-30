from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure

BASE_URL = 'https://sn.rv-school.ru/'
EMPTY_LOGIN_AND_PASSWORD_ERROR = 'Введите телефон, email или логин и пароль.'
LOGIN = 'arkgaranin'
PASSWORD = 'amigo2690'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)  # здесь передается browser, т.к LoginPageHelper наследуется от BasePage,
    # а в BasePage в конструкторе передается драйвер, но сам драйвер мы берем из browser?
    LoginPage.click_login()
    with allure.step('Проверяем на соответствие текста ошибки'):
        assert LoginPage.get_error_text() == EMPTY_LOGIN_AND_PASSWORD_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при вводе логина, но пустом пароле')
def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_username(LOGIN)
    LoginPage.click_login()
    with allure.step('Проверяем на соответствие текста ошибки'):
        assert LoginPage.get_error_text() == EMPTY_LOGIN_AND_PASSWORD_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при вводе пароля, но пустом логине')
def test_empty_login(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_password(PASSWORD)
    LoginPage.click_login()
    with allure.step('Проверяем на соответствие текста ошибки'):
        assert LoginPage.get_error_text() == EMPTY_LOGIN_AND_PASSWORD_ERROR
