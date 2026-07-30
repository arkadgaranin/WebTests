from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationByPhonePageHelper, RegistrationPageHelper
import allure

BASE_URL = 'https://sn.rv-school.ru/'


@allure.suite('Проверка формы регистрации по телефону')
@allure.title('Проверка корректного выбора страны и ее кода из выпадающего списка')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.click_registration_by_phone()
    RegistrationByPhonePage = RegistrationByPhonePageHelper(browser)
    selected_country_and_code = RegistrationByPhonePage.select_random_country_and_code()
    phone_value = RegistrationByPhonePage.get_phone_value()
    with allure.step('Проверяем, что код страны из атрибута присутствует в выбранном значении страны'):
        assert phone_value in selected_country_and_code
