import pytest
import time

from final.pages.login_page import LoginPage
from final.pages.product_page import ProductPage
from final.pages.account_page import AccountPage


@pytest.mark.personal_tests
class TestPersonalTests:
    @pytest.fixture(scope="function", autouse=True)
    def create_user(self, browser):
        login_page = LoginPage(browser, LoginPage.LINK)
        login_page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "H3ll0!^_^"
        login_page.register_new_user(email, password)

        login_page.should_be_authorized_user()
        yield [email, password]

    def test_account_deleting(self, browser, create_user):
        user_credentials = create_user
        account_password = user_credentials[1]
        page = AccountPage(browser, AccountPage.LINK)
        page.open()

        page.delete_account(account_password)
        deleted_account_credentials = user_credentials
        page = LoginPage(browser, LoginPage.LINK)
        page.open()
        page.sign_in(*deleted_account_credentials)

        page.check_disabled_account_sign_in_restriction()


class Skipped:
    #    @pytest.fixture()  # use in rereg
    #    def logout(self):
    #        page = MainPage(...)
    #        page.open()
    #        page.sign_out()

    def test_password_cant_be_changed_on_identical(self):
        page = AccountPage()
        page.open()
        page.click_change_password()
        # page.enter_password
        page.check_password_validation()  # ?
        # page.enter_password
        page.check_changing_password_to_identical_is_restricted()

    def test_unavaliable_product_can_be_added_to_product_alerts(self):
        page = ProductPage(browser, "unavailable_product_link")  # url
        page.click_notify_me()  # inside should_be_no_added_to_basket_button() ... + alert success
        page.go_to_ap()
        page = AccountPage()
        page.go_to_product_alerts()
        # page = ProductAlertsPage()
        page.check_specific_product_was_added_to_product_alerts()

    def test_account_address_prefills_in_checkout(self):
        page = AccountPage()
        page.go_to_address_book()  # should_be_add_addres_button
        page.create_account_address()
        page = ProductPage(browser, ProductPage.LINK)
        page.open()
        page.add_to_basket()
        page.checkout_product()
        page.should_be_prefilled_account_address()

    @pytest.mark.usefixtures("logout")
    def test_registration_on_used_email_is_restricted(self):  # pass creds from fixture
        login_page = LoginPage(browser, LoginPage.LINK)
        login_page.use_registered_email_to_reregister()
        login_page.should_be_reregister_errors()

    def test_email_changes_affect_login(self):
        page = AccountPage()
        page.click_edit_profile()
        page.change_email()  # new value
        page.sign_out()
        page = LoginPage(...)
        page.check_old_email_is_disabled()
        page.check_login_with_new_email()
