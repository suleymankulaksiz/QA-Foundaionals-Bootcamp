from time import sleep
from selenium import webdriver
import pytest
from pages.orders import *
import allure
@pytest.mark.usefixtures("setup")
class TestOrder:
    
    @allure.title('Kategori başlığına göre ürün listelenmesi durumu test edilecektir.')
    def test_viewing_my_past_orders(self):
        order = Orders(self.driver)
        order.login_button_is_clicked()
        order.email_information_is_entered(registeredEmail)
        order.click_on_the_continue_button()
        order.password_information_is_entered(registeredPassword)
        order.click_on_the_login_button()
        order.successful_login_is_verified("QA")
        order.click_my_account()
        order.my_Orders_is_clicked()
        order.verified_that_the_past_orders_page_is_displayed("Siparişlerim")
        
        
    