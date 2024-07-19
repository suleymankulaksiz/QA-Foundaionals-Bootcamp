from time import sleep
from selenium import webdriver
import pytest
from pages.login import *
import allure

@pytest.mark.usefixtures("setup")
class TestLogin:
    @allure.title('Platforma başarılı şekilde giriş yapılması test edilecektir.')
    def test_succes_login(self):
        login = Login(self.driver)
        login.login_button_is_clicked()
        login.email_information_is_entered(registeredEmail)
        login.click_on_the_continue_button()
        login.password_information_is_entered(registeredPassword)
        login.click_on_the_login_button()
        login.successful_login_is_verified("QA")
        
    #kayıtlı olmayan mail giriş testi
    @allure.title('Kayıtlı olmayan mail giriş yapılması test edilecektir.')
    def test_login_with_unregistered_email(self):
        login = Login(self.driver)
        login.login_button_is_clicked()
        login.email_information_is_entered("examplemail@outlook.com")
        login.click_on_the_continue_button()
        login.verify_email_not_found_message("Bu e-posta adresiyle bir hesap bulamıyoruz")
        
    #doğru mail yanlış şifre ile giriş testi
    @allure.title('Doğru mail yanlış şifre ile giriş testi yapılma durumu test edilecektir.')
    def test_login_with_correct_email_and_incorrect_password(self):
        login = Login(self.driver)
        login.login_button_is_clicked()
        login.email_information_is_entered(registeredEmail)
        login.click_on_the_continue_button()
        login.password_information_is_entered("wrongPassword")
        login.click_on_the_login_button()
        login.verify_wrong_password_message("Şifreniz yanlış")
        
    @allure.title('Doldurulması zorunlu alanların boş bırakılma durumu test edilecektir.')
    def test_required_blank_control(self):
        login = Login(self.driver)
        login.login_button_is_clicked()
        login.email_information_is_entered("")
        login.click_on_the_continue_button()
        login.verify_required_email_message_control("E-posta adresinizi veya cep telefonu numaranızı girin")
        login.email_information_is_entered(registeredEmail)
        login.click_on_the_continue_button()
        login.password_information_is_entered("")
        login.click_on_the_login_button()
        login.verify_required_password_message_control("Şifrenizi girin")
        
        