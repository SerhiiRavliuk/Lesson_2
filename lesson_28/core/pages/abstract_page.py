from abc import ABC

from selenium.webdriver.chrome.webdriver import WebDriver
class AbstractPage(ABC):
    _driver : WebDriver

    def __init__(self, driver:WebDriver):
        self._driver = driver
