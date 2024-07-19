from time import sleep
from selenium import webdriver
import pytest
from pages.basket import *
import allure

@pytest.mark.usefixtures("setup")
class TestBasket:
    
    @allure.title('Sepete başarılı bir şekilde ürün eklenmesi test edilecektir.')
    def test1_add_product_to_cart(self):
        basket = Basket(self.driver)
        basket.click_on_the_searchbox_and_search_product("Game laptop")
        basket.click_first_product()
        basket.verify_the_content_of_the_first_clicked_product("MSI NB MODERN 15 B12MO-676XTR I5-1235U 16GB DDR4 UMA 512GB SSD 15.6 FHD DOS SIYAH")
        basket.select_the_standard_package()
        basket.click_on_the_add_to_cart_button()
        basket.verify_the_added_product_in_the_cart("Sepete Eklendi")
        
    @allure.title('Sepetten ürün silme işlemi test edilecektir.')
    def test2_remove_product_from_cart(self):
        basket=Basket(self.driver)
        self.test1_add_product_to_cart()
        basket. click_delete_button()
        basket.click_on_the_go_to_cart_button()
        basket.verify_cart_is_empty("Amazon Sepetiniz boş")
        
    @allure.title('Sepete birden fazla ürün eklenmesi test edilecektir.')
    def test3_add_multiple_products_to_cart(self):
        basket=Basket(self.driver)
        basket.click_on_the_searchbox_and_search_product("laptop")
        basket.click_first_product()
        basket.verify_the_content_of_the_first_clicked_product("MSI NB MODERN 15 B12MO-676XTR I5-1235U 16GB DDR4 UMA 512GB SSD 15.6 FHD DOS SIYAH")
        basket.select_the_standard_package()
        basket.click_on_the_add_to_cart_button()
        basket.verify_the_added_product_in_the_cart("Sepete Eklendi")
        basket.click_on_the_searchbox_and_search_product("SAMSUNG Galaxy Z Flip6")
        basket.click_first_product()
        basket.click_on_the_add_to_cart_button()
        basket.cart_contents_are_verified("Ara toplam (2 ürün):")
        
        
       
        
        