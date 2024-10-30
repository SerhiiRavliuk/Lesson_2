import pytest
from Lesson_28.pages.registration_page import RegistrationPage

def test_user_registration(login_to_site, driver):

    registration_page = RegistrationPage(driver)

    registration_page.click_sign_in()

    registration_page.input_name("Max")
    registration_page.input_last_name("Ravliuk")
    registration_page.input_email("max.ravliukkkkk@gmail.com")
    registration_page.input_password("Password123")
    registration_page.input_reenter_password("Password123")
    registration_page.submit()

    success_message = registration_page.get_success_message()
    assert "Log out" in success_message
