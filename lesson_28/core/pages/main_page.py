import allure
from assertpy import assert_that
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.web_elements.button import Button


class MainPage(AbstractPage):

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    logged_in_attributes_locators:tuple [str,str] = (By.XPATH, ".//li[./a[text()=' Logout' or text()=' Logged in as ']]")

    @property
    def signup_and_login_button(self) -> Button:
        return Button(self._driver,(By.XPATH, ".//li[./a[text() = ' Signup / Login']]"))

    @property
    def logged_out_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//li[./a[text()=' Logout']]"))

    @property
    def contact_us_button(self) -> Button:
        return Button(self._driver, (By.XPATH, (".//li[./a[text() = ' Contact us']]")))


    @allure.step("Go to SignUp and LogIn page")
    def go_to_signup_and_login_page(self):
        self.signup_and_login_button.click()


    def go_to_contact_us_page(self):
        self.contact_us_button.click()

    @allure.step("Logged out")
    def logged_out(self):
        self.logged_out_button.click()

    @allure.step("Verify that user logged out")
    def verify_that_user_logged_out(self):
        assert_that(self.signup_and_login_button.wait_for_visible()).is_true()


    # @property
    # def logged_in_attributes(self) -> list[WebElement]:
    #     return self._wrapped_element.find_elements(self.logged_in_attributes_locators)

    # def verify_that_user_logged_in(self):
    #     assert_that(len(self.logged_in_attributes) == 2).is_true()
    #     assert_that(all([element.is_displayed() for element in self.logged_in_attributes])).is_true()