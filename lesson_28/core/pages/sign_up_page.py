import allure
from assertpy import assert_that
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.web_elements.input_field import InputField


class SignUpPage(AbstractPage):

    def __init__(self,driver:WebDriver):
        super().__init__(driver)

    @property
    def sign_up_page_element(self) -> WebElement:
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id = 'id_gender1']"))
        )

    @allure.step("Verify that user is placed on SignUp page")
    def verify_that_user_is_placed_on_sign_up_page(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of(self.sign_up_page_element))



