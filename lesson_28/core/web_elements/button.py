from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.core.web_elements.abstract_element import AbstractElement


class Button(AbstractElement):

    def __init__(self,driver: WebDriver, locator:tuple[str,str]):
        super().__init__(driver,locator)

    def click(self):
        return self.wait_to_be_clickable().click()
