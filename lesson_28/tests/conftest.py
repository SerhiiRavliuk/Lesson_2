import pytest
from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chromium.options import ChromiumOptions

from lesson_28.core.test_data.test_data import TestData


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Правильний імпорт

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def web_driver_creation():
    # chrome_options = webdriver.ChromeOptions()
    #
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:8080/wd/hub',
    #     options=chrome_options
    # )
    driver : WebDriver = webdriver.Chrome()
    driver.get(TestData.BASE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()

