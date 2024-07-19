from selenium.webdriver.common.by import By
import random
import string

def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])

        extension = random.choice(['com', 'net', 'org'])

        extension = random.choice(['com', 'net', 'org'])                                       #burada random mail oluşturma işlemi yapıyoruz.

    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom

email ="denemehesabi299@outlook.com"
password ="tester159753SK"
password_again="tester159753SK"
name_surname ="QA Foundations Bootcamp"
alreadyMail="slymann89@outlook.com"

BASE_URL ="https://www.amazon.com.tr/"

CLICK_LOGIN_BUTTON_LOCATOR ="//a[@id='nav-link-accountList']/span"
CLICK_SIGNUP_BUTTON_LOCATOR ="createAccountSubmit"
REGISTER_TEXT_LOCATOR ="[class='form-title font-bold text-sm text-gray-600 font-base mb-4']"
NAME_INPUT_LOCATOR ="ap_customer_name"
VERIFICATION_LOGIN_HEADER ="//*[@id='ap_register_form']/div/div/h1"

EMAIL_INPUT_LOCATOR ="ap_email"
PASSWORD_INPUT_LOCATOR="ap_password"
PASSWORD_INPUT_AGAIN_LOCATOR="ap_password_check"

REQUIRED_BLANK_ASSERT_LOCATOR = "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/div/div/div"
PASSWORD_ALERT_ASSERT_LOCATOR = "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[2]/div[2]/div/div"
MIN_CHR_ALERT_ASSERT_LOCATOR = "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/div[4]/div/div"
INVALID_EMAIL_ALERT_ASSERT_LOCATOR = "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div/div[2]/div/div"
ALREADY_REGISTERED_EMAIL_ALERT_ASSERT_LOCATOR = "/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span"
PASWORD_TYPE_ALERT_ASSERT_LOCATOR  ="/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/input"

SIGNUP_BUTTON_LOCATOR="continue"

IFRAME_XPATH="//iframe[@title='reCAPTCHA']"
CAPTCHA_XPATH = "//*[@id='recaptcha-anchor']"