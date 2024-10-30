import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button"))
        )
        sign_in_button.click()

    def input_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signupName"]'))
        )
        name_input.send_keys(name)

    def input_last_name(self, last_name):
        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signupLastName"]'))
        )
        last_name_input.send_keys(last_name)

    def input_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signupEmail"]'))
        )
        email_input.send_keys(email)

    def input_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signupPassword"]'))
        )
        password_input.send_keys(password)

    def input_reenter_password(self, password):
        reenter_password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signupRepeatPassword"]'))
        )
        reenter_password_input.send_keys(password)

    def submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button"))
        )
        submit_button.click()
        time.sleep(1)
        print("Form submitted, waiting for success message...")

    def get_success_message(self):
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[4]"))
            )
            print("Success message found:", success_message.text)
            return success_message.text
        except Exception as e:
            print(f"Error finding success message: {e}")
            return None

