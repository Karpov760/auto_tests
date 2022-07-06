from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_same_names(self):
        assert self.get_element_text(*ProductPageLocators.NAME) == self.get_element_text(*ProductPageLocators.ADDED_NAME), "Names are not the same"

    def should_be_same_prices(self):
        assert self.get_element_text(*ProductPageLocators.PRICE) == self.get_element_text(*ProductPageLocators.ADDED_PRICE), "Prices are not the same"