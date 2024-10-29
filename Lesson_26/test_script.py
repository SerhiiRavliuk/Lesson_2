from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000')
    yield driver
    driver.quit()

def verify_frame(driver, frame_id, secret_text):
    print(f"Перемикаємося на {frame_id}")
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    input_field = driver.find_element(By.ID, f'input{frame_id[-1]}')
    print(f"Знайдено поле вводу для {frame_id}")

    input_field.send_keys(secret_text)
    verify_button = driver.find_element(By.XPATH, '//button[contains(text(), "Перевірити")]')
    print(f"Натискаємо кнопку 'Перевірити' для {frame_id}")

    verify_button.click()

    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f'Alert from {frame_id}: {alert_text}')
    alert.accept()

    driver.switch_to.default_content()

def test_frames(setup):
    driver = setup
    verify_frame(driver, "frame1", "Frame1_Secret")
    verify_frame(driver, "frame2", "Frame2_Secret")
