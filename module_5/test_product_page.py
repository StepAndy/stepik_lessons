import pytest
from module_5.pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2",
                              "offer3", "offer4", "offer5",
                              "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        new_link = link + promo_offer
        print(new_link)
        page = ProductPage(browser, new_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_specific_product_was_added_to_basket()
        page.check_basket_and_product_costs_are_equal()
