from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локаторы тулбара с сайта ОК, т.к на сайте https://sn.rv-school.ru/ нет такого тулбара
    LOGO_BUTTON = (By.ID, 'nohook_logo_link')
    VK_ECOSYSTEM_BUTTON = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f"Не удалось найти элеменет{locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f"Не удалось найти элеменеты{locator}")

    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenschot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step('Нажимаем кнопку экосистемы')
    def click_vk_ecosystem(self):
        self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON).click()
        self.attach_screenschot()

    @allure.step('Нажимаем кнопку "Еще"')
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()
        self.attach_screenschot()

    @allure.step('Получаем id вкладки браузера')
    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переключаемся на вкладку браузера')
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)
        self.attach_screenschot()
