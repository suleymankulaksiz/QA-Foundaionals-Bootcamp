from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class PageBase:

    def __init__(self, driver):
        self.driver = driver
        

    

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return element
    def wait_for_element_visible(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located((by, value)))
    def cookie(self):
        cookie_button = self.driver.find_element(By.ID, "sp-cc-accept")
        cookie_button.click()
        