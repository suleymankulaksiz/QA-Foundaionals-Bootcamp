from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.register_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class Register(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    
       
        
        
    def login_button_is_clicked(self):
        clickLoginButton = self.driver.find_element(By.XPATH,CLICK_LOGIN_BUTTON_LOCATOR)
        clickLoginButton.click()
        
        
    def create_account_button_is_clicked(self):
        clickSignUpButton = self.driver.find_element(By.ID,CLICK_SIGNUP_BUTTON_LOCATOR)
        clickSignUpButton.click()
        header_name = self.driver.find_element(By.XPATH, VERIFICATION_LOGIN_HEADER)
        header_text = header_name.text
        assert header_text == "Hesap oluşturun", f"Header '{header_text}' Expected 'Hesap oluşturun', not this."
    
    def name_surname_information_is_entered(self,name):
        nameInput = self.driver.find_element(By.ID, NAME_INPUT_LOCATOR)
        nameInput.send_keys(name)
    
    
        
    def email_information_is_entered(self):
        emailrandom = generate_random_email()
        emailInput = self.driver.find_element(By.ID, EMAIL_INPUT_LOCATOR)
        emailInput.send_keys(emailrandom)
        
    def already_registered_is_entered(self,alreadyMail):
        emailInput = self.driver.find_element(By.ID, EMAIL_INPUT_LOCATOR)
        emailInput.send_keys(alreadyMail)
        
    def invalid_email_information_is_entered(self,emaill):
        emailInput = self.driver.find_element(By.ID, EMAIL_INPUT_LOCATOR)
        emailInput.send_keys(emaill)
    
    def password_information_is_entered(self,password):
        passwordInput = self.driver.find_element(By.ID, PASSWORD_INPUT_LOCATOR)
        passwordInput.send_keys(password)
    
    def password_information_is_entered_one_more_time(self,password):
        passwordConfirmInput = self.driver.find_element(By.ID, PASSWORD_INPUT_AGAIN_LOCATOR)
        passwordConfirmInput.send_keys(password)
        
        
    def required_blank_error_message_is_displayed(self,alertMessage):
        required_blank = self.driver.find_element(By.XPATH,REQUIRED_BLANK_ASSERT_LOCATOR)
        assert required_blank.text == alertMessage,"The required fields empty message was not displayed."
        
    def checking_password_mismatch_condition(self,alertMessage):
        password_alert = self.driver.find_element(By.XPATH,PASSWORD_ALERT_ASSERT_LOCATOR)
        assert password_alert.text == alertMessage,"The warning message indicating that the messages do not match was not displayed."
        

        
    def sign_up_confirm_button_clicked(self):
        signUpConfirmButton = self.driver.find_element(By.ID,SIGNUP_BUTTON_LOCATOR)
        signUpConfirmButton.click()
        
    def minimum_character_password_check(self,alertMessage):
        minChr = self.driver.find_element(By.XPATH,MIN_CHR_ALERT_ASSERT_LOCATOR)
        assert minChr.text == alertMessage,"The min character password message was not displayed."
        
    def reCAPTCHA_button_clicked(self):
        
        sleep(15)#This waiting is for the reCAPTCHA puzzle/visual verification
        
        # iframe = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, IFRAME_XPATH)))
        # self.driver.switch_to.frame(iframe)                                                                           69-72 These lines of code are for clicking the reCAPTCHA verification.      
        # captcha = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,CAPTCHA_XPATH)))
        # captcha.click()
        
        
    
        
    def invalid_email_error_message_is_displayed(self,alertMessage):
        invalidEmail = self.driver.find_element(By.XPATH,INVALID_EMAIL_ALERT_ASSERT_LOCATOR)
        assert invalidEmail.text == alertMessage,"The invalid email message was not displayed."
        
    def already_registered_email_error_message_is_displayed(self,alertMessage):
        alreadyRegisteredEmail = self.driver.find_element(By.XPATH,ALREADY_REGISTERED_EMAIL_ALERT_ASSERT_LOCATOR )
        assert alreadyRegisteredEmail.text == alertMessage,"The already registered email message was not displayed."
        
    def masked_password_check(self,alertMessage):
        password_type = self.wait_for_element_visible(By.XPATH, PASWORD_TYPE_ALERT_ASSERT_LOCATOR).get_attribute("type")
        assert password_type == alertMessage, "Password is not masked." 
        
                
   
  
    
        
        
        

    