import time

import allure
import pytest

from lesson_28.core.pages.contact_us_page import ContactUsPage
from lesson_28.core.pages.sign_up_and_login_page import SignUpAndLoginPage
from lesson_28.core.pages.main_page import MainPage
from lesson_28.core.pages.sign_up_page import SignUpPage
from lesson_28.core.test_data.test_data import TestData

@allure.feature("Testing Automation exercise cite")
class TestAutomation:
    main_page : MainPage
    signup_and_login_page : SignUpAndLoginPage
    contact_us_page : ContactUsPage
    signup_page : SignUpPage

    @allure.story("Go to login page and login")
    def test_that_user_can_log_in(self, web_driver_creation):
        self.main_page = MainPage(web_driver_creation)
        self.signup_and_login_page = SignUpAndLoginPage(self.main_page.go_to_signup_and_login_page())
        self.signup_and_login_page = SignUpAndLoginPage(web_driver_creation)
        self.signup_and_login_page.fill_log_in_fields_and_log_in(TestData.LOGIN_EMAIL,TestData.LOGIN_PASSWORD)

        time.sleep(1)

    # @allure.story("Logged out")
    # def test_that_user_can_logged_out(self, web_driver_creation):
    #     self.main_page = MainPage(web_driver_creation)
    #     self.main_page.logged_out()
    #     self.main_page.verify_that_user_logged_out()
    #
    # @allure.story("Go to signup page and signup")
    # def test_navigate_to_sign_in_page_and_sign_in(self, web_driver_creation):
    #     self.main_page = MainPage(web_driver_creation)
    #     self.main_page.go_to_signup_and_login_page()
    #     self.signup_and_login_page = SignUpAndLoginPage(web_driver_creation)
    #     self.signup_and_login_page.fill_sign_up_fields_and_sign_up(TestData.USER_VALID_NAME, TestData.USER_VALID_EMAIL)
    #     self.signup_page = SignUpPage(web_driver_creation)
    #     self.signup_page.verify_that_user_is_placed_on_sign_up_page()
    #
    #
    # @allure.story("Test for issue vizualization")
    # @allure.issue('https://github.com/DartBrovsky/aqa_python_hillel/blob/main/lesson_30/test_initial.py',"test allure issue with link on github")
    # @pytest.mark.skip
    # def test_allure_issue_with_link_on_github(self):
    #     assert False









