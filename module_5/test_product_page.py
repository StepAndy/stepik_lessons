import pytest

from module_5.pages.login_page import LoginPage
from module_5.pages.product_page import ProductPage
from module_5.pages.basket_page import BasketPage


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2",
                              "offer3", "offer4", "offer5",
                              "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        full_promo_link = ProductPage.LINK + '?promo=' + promo_offer
        page = ProductPage(browser, full_promo_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_specific_product_was_added_to_basket()
        page.check_basket_and_product_costs_are_equal()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.add_to_basket()
        page.check_success_message_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_products_in_basket()
        basket_page.should_be_text_basket_is_empty()
