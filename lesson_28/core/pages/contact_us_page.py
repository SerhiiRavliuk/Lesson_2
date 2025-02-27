from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.web_elements.input_field import InputField

class ContactUsPage(AbstractPage):

    def __init__(self, driver: WebDriver):
            super().__init__(driver)

    @property
    def bottom_email_field(self) -> InputField:
            return InputField(self._driver, (By.XPATH, ".//input[@placeholder = 'Your email address']"))

    def scroll_to_bottom_email_field(self):
        self._driver.execute_script("arguments[0].scrollIntoView(true);", self.bottom_email_field._wrapped_element)

