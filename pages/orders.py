from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.orders_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class Orders(PageBase):
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
        
    def click_my_account(self):
        myAccount = self.driver.find_element(By.ID, "nav-link-accountList")
        myAccount.click()
    
    def my_Orders_is_clicked(self):
        myOrders = self.driver.find_element(By.XPATH, "//*[@id='a-page']/div[1]/div/div[2]/div[1]/a/div/div/div/div[2]/h2")
        myOrders.click()
        
    def verified_that_the_past_orders_page_is_displayed(self,assertMessage):
        login_success = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div[1]")
        assert_text = login_success.text
        assert assert_text == assertMessage, f"Expected text to be 'Siparişlerim' but got '{assert_text}'"