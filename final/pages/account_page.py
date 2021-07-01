import pytest
from selenium.common.exceptions import NoSuchElementException

from final.pages.base_page import BasePage
from final.pages.locators import AccountPageLocators


class AccountPage(BasePage):
    LINK = 'https://selenium1py.pythonanywhere.com/accounts/'

    def delete_account(self, password):
        try:
            self.browser.find_element(
                *AccountPageLocators.DELETE_PROFILE).click()
            self.browser.find_element(
                *AccountPageLocators.DELETE_PROFILE_PASSWORD).send_keys(password)
            self.browser.find_element(
                *AccountPageLocators.CONFIRM_DELETE).click()
        except NoSuchElementException:
            pytest.fail("Some of delete account controls weren't found")

    def create_new_password_identical_to_old(self, old_pass):
        try:
            self.browser.find_element(
                *AccountPageLocators.CHANGE_PASSWORD).click()
            for inputs in self.browser.find_elements_by_css_selector(
                    "input[required]"):
                inputs.send_keys(old_pass)
            self.browser.find_element(
                *AccountPageLocators.CONFIRM_CHANGE_PASSWORD).click()
        except NoSuchElementException:
            pytest.fail("Some of change password controls weren't found")

    def check_new_passwrod_differs_from_old(self):
        assert self.is_not_element_present(
            *AccountPageLocators.PASSWORD_UPDATED)
