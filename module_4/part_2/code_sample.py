import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'
delete_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/delete/'

registration_form = {
    'login_link_locator': (By.ID, 'login_link'),
    'email_input_locator': (By.ID, 'id_registration-email'),
    'pswd_input_locator': (By.ID, 'id_registration-password1'),
    'confirm_pswd_input_locator': (By.ID, 'id_registration-password2'),
    'registration_button_locator': (By.NAME, 'registration_submit')
}
post_registration_alert = (By.CSS_SELECTOR, ".alertinner.wicon")
confirm_delete_input = (By.NAME, "password")
confirm_delete_button = (By.CSS_SELECTOR, ".btn-danger")

test_email = 'test@registration.com'
test_password = 'qqq111!!!'


def delete_profile(driver):
    driver.find_element(*confirm_delete_input).send_keys(test_password)
    driver.find_element(*confirm_delete_button).click()


def fill_registration_form(driver):
    driver.find_element(
        *registration_form['email_input_locator']).send_keys(test_email)
    driver.find_element(
        *registration_form['pswd_input_locator']).send_keys(test_password)
    driver.find_element(
        *registration_form['confirm_pswd_input_locator']).send_keys(test_password)


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.get(delete_link)
    delete_profile(browser)
    browser.quit()


def test_registration(browser):
    browser.get(link)
    login_link = browser.find_element(
        *registration_form['login_link_locator'])
    login_link.click()

    fill_registration_form(browser)
    registration_button = browser.find_element(
        *registration_form['registration_button_locator'])
    registration_button.click()

    assert browser.find_element(*post_registration_alert).text == \
           'Thanks for registering!', "No successful registration alert was found"
