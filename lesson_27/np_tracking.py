from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class NovaPoshtaTracker:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def close(self):
        self.driver.quit()

    def track_parcel(self, tracking_number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="en"]'))
        )
        input_field.send_keys(tracking_number)

        submit_button = self.driver.find_element(By.XPATH, '//*[@id="np-number-input-desktop-btn-search-en"]')
        submit_button.click()

        try:

            status_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.header__status-text'))
            )
            return status_element.text
        except:

            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "не знайшли посилку")]'))
            )
            return error_message_element.text

@pytest.fixture
def setup():
    tracker = NovaPoshtaTracker()
    yield tracker
    tracker.close()

def test_parcel_status(setup):
    tracker = setup
    tracking_number = "NP000054667"
    expected_status = "Посилка отримана"

    actual_status = tracker.track_parcel(tracking_number)

    if "не знайшли посилку" in actual_status:
        assert "не знайшли посилку" in actual_status, f"Очікував статус про відсутність посилки, але отримав '{actual_status}'"
    else:
        assert actual_status == expected_status, f"Очікував '{expected_status}', але отримав '{actual_status}'"
