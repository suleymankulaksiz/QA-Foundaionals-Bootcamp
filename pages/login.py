from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.login_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class Login(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def login_button_is_clicked(self):
        clickLoginButton = self.driver.find_element(By.XPATH,CLICK_LOGIN_BUTTON_LOCATOR)
        clickLoginButton.click()
        
    def email_information_is_entered(self,email):
        emailInput = self.driver.find_element(By.ID, EMAIL_INPUT_LOCATOR)
        emailInput.send_keys(email)
    
    def click_on_the_continue_button(self):
        clickContinueButton = self.driver.find_element(By.ID, CLICK_CONTINUE_BUTTON_LOCATOR)
        clickContinueButton.click()
        
    def password_information_is_entered(self, password):
        passwordInput = self.driver.find_element(By.ID, PASSWORD_INPUT_LOCATOR)
        passwordInput.send_keys(password)
    
    def click_on_the_login_button(self):
        clickLoginButton = self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR)
        clickLoginButton.click()
    
    def successful_login_is_verified(self,assertMessage):
        login_success = self.driver.find_element(By.ID, LOGIN_SUCCESS_ALERT_MESSAGE)
        assert_text = login_success.text
        assert assert_text == assertMessage, f"Expected text to be 'QA' but got '{assert_text}'"
        
    def verify_email_not_found_message(self,assertMessage):
        email_not_found = self.driver.find_element(By.XPATH, EMAIL_NOT_FOUND_ALERT_MESSAGE)
        assert email_not_found.text == assertMessage, "The email not found message was not displayed."
        
    def verify_wrong_password_message(self,assertMessage):
        wrong_password = self.driver.find_element(By.XPATH, WRONG_PASSWORD_ALERT_MESSAGE)
        assert wrong_password.text == assertMessage, "The password not found message was not displayed."
        
    def verify_required_email_message_control(self,assertMessage):
        required_area = self.driver.find_element(By.ID, REQUIRED_AREA_EMAIL_ALERT_MESSAGE)
        assert required_area.text == assertMessage, "The email area not found message was not displayed."
    
    def verify_required_password_message_control(self,assertMessage):
        required_area = self.driver.find_element(By.ID, REQUIRED_AREA_PASSWORD_ALERT_MESSAGE)
        assert required_area.text == assertMessage, "The password area not found message was not displayed."
        