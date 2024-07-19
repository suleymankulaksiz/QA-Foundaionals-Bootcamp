from time import sleep
from selenium import webdriver
import pytest
from pages.register import *
import allure

@pytest.mark.usefixtures("setup")
class TestRegister:
    
    #başarılı kayıt olma senaryosu
    @allure.title('Platforma başarılı şekilde kayıt olma işlemi test edilecektir.')
    def test_success_register(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked() 
        register_page.name_surname_information_is_entered(name_surname)                                             
        register_page.email_information_is_entered()
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time(password_again)
        register_page.sign_up_confirm_button_clicked()
        register_page.reCAPTCHA_button_clicked()
        
    @allure.title('Doldurulması zorunlu alanların boş bırakıldığı durum test edilecektir.')
    def test_required_blank_control(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered("")
        register_page.email_information_is_entered()
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time(password_again)
        register_page.sign_up_confirm_button_clicked()
        register_page.required_blank_error_message_is_displayed("Adınızı girin"), 
     
    @allure.title('Şifrelerin eşleşmediği durum test edilecektir.') 
    def test_checking_password_mismatch_condition(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered(name_surname)
        register_page.email_information_is_entered()
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time("123456789")
        register_page.sign_up_confirm_button_clicked()
        register_page.checking_password_mismatch_condition("Şifreler eşleşmiyor"),
        
    @allure.title('Geçersiz mail ile kayıt olma durumu test edilecektir.')
    def test_invalid_email_control(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered(name_surname)
        register_page.invalid_email_information_is_entered("testtest")
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time(password_again)
        register_page.sign_up_confirm_button_clicked()
        register_page.invalid_email_error_message_is_displayed("Geçerli bir e-posta adresi girin"), 
        
    @allure.title('Şifre alanının minimum karakter ile kayıt olma durumu test edilecektir.')
    def test_min_character_control(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered(name_surname)
        register_page.email_information_is_entered()
        register_page.password_information_is_entered("1")
        register_page.password_information_is_entered_one_more_time("1")
        register_page.sign_up_confirm_button_clicked()
        register_page.minimum_character_password_check("Şifreler en az 6 karakterden oluşmalıdır.") 

    @allure.title('Platforma kayıtlı mail ile kayıt olunabilme durumu test edilecektir.')
    def test_signing_up_with_registered_email_address(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered(name_surname)
        register_page.already_registered_is_entered(alreadyMail)
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time(password_again)
        register_page.sign_up_confirm_button_clicked()
        register_page.already_registered_email_error_message_is_displayed("Yeni bir müşteri olduğunuzu belirttiniz ancak slymann89@outlook.com adresi ile kayıtlı bir hesap var")
    
    @allure.title('Girilen şifrenin maskelendiği durum test edilecektir.')
    def test_masked_password_control(self):
        register_page = Register(self.driver)
        register_page.login_button_is_clicked()
        register_page.create_account_button_is_clicked()
        register_page.name_surname_information_is_entered(name_surname)
        register_page.email_information_is_entered()
        register_page.password_information_is_entered(password)
        register_page.password_information_is_entered_one_more_time(password_again)
        register_page.masked_password_check("password")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
       
        