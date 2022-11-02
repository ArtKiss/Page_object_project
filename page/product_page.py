import time

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE), "Product page is not presented"

    def should_be_the_same_price(self):
        alert_name = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[0].text
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        assert alert_name == name, "The name in the basket does not match"

    def should_be_the_same_book_name(self):
        alert_price = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[2].text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert alert_price == price, "The price in the basket does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_LIST), "Success message is presented, but " \
                                                                             "should not be "

    def should_see_as_disappearing_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_LIST), "Success message is not disappeared"
