from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET), "Basket is empty"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PROMO_CODE), "Basket is empty"
