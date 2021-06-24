from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT),\
            "There are products in basket"

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            "Text saying basket is empty was not found"

