import pytest

from module_5.pages.product_page import ProductPage

promo_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='
link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2",
                              "offer3", "offer4", "offer5",
                              "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        full_promo_link = promo_link + promo_offer
        page = ProductPage(browser, full_promo_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_specific_product_was_added_to_basket()
        page.check_basket_and_product_costs_are_equal()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_success_message_disappeared()
