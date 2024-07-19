from time import sleep
from selenium import webdriver
import pytest
from pages.productDetails import *
import allure
@pytest.mark.usefixtures("setup")
class TestProductDetails:
    
    @allure.title('Listelenen ürün ve seçilen ürünün aynı olduğu durum test edilecektir.')
    def test_compatibilit_selected_product_contents(self):
        pDetails= ProductDetails(self.driver)
        pDetails.click_on_the_searchbox_and_search_product("Apple iPhone 15 Pro")
        pDetails.click_first_product()
        pDetails.verify_the_content_of_the_first_clicked_product("Apple iPhone 15 Pro (128 GB) - Mavi Titanyum")
    
    @allure.title('Ürün ile ilgili değerlendirilmelerin görüntülenmesi test edilecektir.')
    def test_see_product_ratings(self):
        pDetails= ProductDetails(self.driver)
        self.test_compatibilit_selected_product_contents()
        pDetails.product_rating_scores_are_verified("253 değerlendirme")
    
    @allure.title('Ürün hakkında yorumların sayfasının görüntülenmesi test edilecektir.')
    def test_product_reviews(self):
        pDetails= ProductDetails(self.driver)
        self.test_compatibilit_selected_product_contents()
        pDetails.click_on_the_review_button()
        pDetails.verified_that_the_product_reviews_are_displayed("Şu ülkeden en iyi değerlendirmeler: Türkiye")
        sleep(3)
    
        
        
        
        