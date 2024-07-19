from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.basket_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class Basket(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def click_on_the_searchbox_and_search_product(self,item):
        self.driver.find_element(By.ID,SEARCHBOX_LOCATOR).send_keys(item)
        searchbox_button = self.driver.find_element(By.ID,SEARCHBOX_BUTTON_LOCATOR)
        searchbox_button.click()
        
    def click_first_product(self):
        first_product = self.driver.find_element(By.CSS_SELECTOR, FIRST_PRODUCT_LOCATOR)
        first_product.click()
        
    def click_item(self):
        item = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div[1]/span/a/div/img")
        item.click()
        
    
    def verify_the_content_of_the_first_clicked_product(self,alertMessage):
        first_item_name = PageBase(self.driver).wait_for_element_visible(By.XPATH, FIRST_ITEM_NAME_LOCATOR)
        assert first_item_name.text == alertMessage, "The product name not correct."
        
    def select_the_standard_package(self):
        standart = self.driver.find_element(By.XPATH,STANDART_PACKAGE_LOCATOR)
        standart.click()
    
    def click_on_the_add_to_cart_button(self):
        add_to_cart_button = PageBase(self.driver).wait_for_element_visible(By.ID, ADD_CART_BUTTON_LOCATOR)
        add_to_cart_button.click()
    
    def verify_the_added_product_in_the_cart(self,alertMessage):
        added_product = self.driver.find_element(By.XPATH,ADD_PRODUCT_ASSERT_LOCATOR)
        assert added_product.text == alertMessage, "The product was added unsuccessfull"
    
    def click_on_the_go_to_cart_button(self):
        go_to_cart_button = PageBase(self.driver).wait_for_element_visible(By.XPATH, GO_TO_CART_BUTTON_LOCATOR)
        go_to_cart_button.click()
    
    
    
    def click_delete_button(self):
        delete_button = PageBase(self.driver).wait_for_element_visible(By.XPATH, DELETE_BUTTON_LOCATOR)
        delete_button.click()

    
    def verify_cart_is_empty(self,assertMessage):
        empty_basket =  PageBase(self.driver).wait_for_element_visible(By.XPATH,EMPTY_BASKET_LOCATOR)
        assert empty_basket.text == assertMessage, "The cart is not empty"
    
    def cart_contents_are_verified(self,assertMessage):
        go_to_basket = PageBase(self.driver).wait_for_element_visible(By.XPATH,GO_TO_BASKET_LOCATOR)
        go_to_basket.click()
        assert_text= PageBase(self.driver).wait_for_element_visible(By.XPATH,MULTI_ASSERT_TEXT_LOCATOR)
        assert assert_text.text == assertMessage,"The cart content is not correct."
    