from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationByPhonePageHelperHelper, RegistrationPageHelperHelper, EnteringCodeFromSmsPageHelperHelper
import allure

BASE_URL = 'https://sn.rv-school.ru/'


@allure.suite('Проверка формы регистрации по телефону')
@allure.title('Проверка корректного выбора страны и ее кода из выпадающего списка')
def test_registration_by_phone(browser, generate_random_phone_number):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    RegistrationPage.click_registration_by_phone()
    RegistrationByPhonePage = RegistrationByPhonePageHelperHelper(browser)
    phone_value = RegistrationByPhonePage.select_random_country_and_code()
    RegistrationByPhonePage.enter_phone(generate_random_phone_number)
    RegistrationByPhonePage.click_get_code_button()
    EnteringCodeFromSmsPage = EnteringCodeFromSmsPageHelperHelper(browser)
    phone_number_text = EnteringCodeFromSmsPage.get_phone_number_text()

    with allure.step('Проверяем, что код страны из атрибута присутствует в тексте номера телефона'):
        assert phone_value in phone_number_text
