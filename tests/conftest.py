from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from constants.register_loc import *
from pages.PageBase import *

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    PageBase(driver).cookie()
    request.cls.driver = driver
    yield
    driver.quit()

    
