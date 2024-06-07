import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pom import LoginPage

def test_login(browser):
    login_page=LoginPage(browser)
    login_page.login()