import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_to_site(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
