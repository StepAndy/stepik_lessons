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
