from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def check_specific_product_was_added_to_basket(self):
        product_name = self.get_product_name()
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert, \
            f"Alert must contain product '{product_name}', but got '{product_name_in_alert}'"

    def check_basket_and_product_costs_are_equal(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_cost == basket_cost, \
            "Basket and product costs must be equal after adding to the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)