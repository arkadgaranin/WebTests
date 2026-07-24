import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def browser():
    driver_path = r"C:\Users\Arkady\chrome-webdriver\yandex\yandexdriver.exe"
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome() # в тест-хроме почему-то нет некоторых кнопок на сайте ОК
    yield driver
    driver.quit()
