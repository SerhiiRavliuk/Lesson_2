import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.pages.main_page import MainPage
from lesson_28.core.test_data.test_data import TestData
from lesson_28.core.web_elements.button import Button
from lesson_28.core.web_elements.input_field import InputField


class SignUpAndLoginPage(AbstractPage):

    def __init__(self,driver:WebDriver):
        super().__init__(driver)

    @property
    def sign_up_name_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, '//input[@data-qa="signup-name"]'))

    @property
    def sign_up_email_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, '//input[@data-qa="signup-email"]'))

    @property
    def sign_up_button(self) -> Button:
        return Button(self._driver,(By.XPATH,'//button[@data-qa="signup-button"]'))

    @property
    def log_in_email_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, "//input[@data-qa='login-email']"))

    @property
    def log_in_password_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, "//input[@data-qa='login-password']"))

    @property
    def log_in_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//button[@data-qa = 'login-button']") )

    @property
    def main_page(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//li[./a[text() = ' Home']]"))

    def go_to_main_page(self):
        self.main_page.click()
        return MainPage(self._driver)

    @allure.step("Fill in LogIn fields")
    def fill_log_in_fields_and_log_in(self, email:str, password:str):
        self.log_in_email_field.fill(email)
        self.log_in_password_field.fill(password)
        self.log_in_button.click()

    @allure.step("Fill in SignUp fields")
    def fill_sign_up_fields_and_sign_up(self,name:str, email:str):
        self.sign_up_name_field.fill(name)
        self.sign_up_email_field.fill(email)
        self.sign_up_button.click()







