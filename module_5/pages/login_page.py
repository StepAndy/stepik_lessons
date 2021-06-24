import pytest
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    LINK = 'https://selenium1py.pythonanywhere.com/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_substring = "login"
        assert url_substring in self.browser.current_url, \
            f"Page's url must contain '{url_substring}' in it"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Registration form is not present"

    def click_submit(self):
        try:
            self.browser.find_element(*LoginPageLocators.SUBMIT).click()
        except NoSuchElementException:
            pytest.fail("Submit button is missing")

    def fill_registration_form(self, email, password):
        try:
            self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
            self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        except NoSuchElementException:
            pytest.fail("One of required fields is missing")

    def register_new_user(self, email, password):
        self.fill_registration_form(email, password)
        self.click_submit()
