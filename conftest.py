import pytest
from selenium import webdriver

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="module")  #fixture will be executed once per module.
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()