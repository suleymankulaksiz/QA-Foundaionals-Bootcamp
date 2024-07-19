from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.productDetails_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class ProductDetails(PageBase):
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
    
    def verify_the_content_of_the_first_clicked_product(self,assertMessage):
        first_item_name = PageBase(self.driver).wait_for_element_visible(By.XPATH, FIRST_ITEM_NAME_LOCATOR)
        assert first_item_name.text == assertMessage, "The product name not correct."
        
    def product_rating_scores_are_verified(self,assertMessage):
        rating = self.driver.find_element(By.XPATH, RATING_LOCATOR)
        rating.click()
        sleep(2)
        self.driver.save_screenshot("images/product_rating.png")
        rating_total = PageBase(self.driver).wait_for_element_visible(By.ID, RATING_TOTA_LOCATOR)
        assert rating_total.text == assertMessage, "The product name not correct."
    
    def click_on_the_review_button(self):
        rating_total = PageBase(self.driver).wait_for_element_visible(By.ID, RATING_TOTA_LOCATOR)
        rating_total.click()

    def verified_that_the_product_reviews_are_displayed(self,assertMessage):
        reviews = self.driver.find_element(By.XPATH, REVIEWS_LOCATOR)
        assert reviews.text == assertMessage, "Product reviews were not displayed"
    