from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=60):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f"Не удалось найти элеменет{locator}")

    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenschot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)
