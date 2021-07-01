from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class AccountPageLocators:
    DELETE_PROFILE = (By.CSS_SELECTOR, "#delete_profile")
    DELETE_PROFILE_PASSWORD = (By.CSS_SELECTOR, "#id_password")
    CONFIRM_DELETE = (By.CSS_SELECTOR, ".btn.btn-lg.btn-danger")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    SUBMIT = (By.NAME, 'registration_submit')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    SIGN_IN_BUTTON = (By.NAME, 'login_submit')
    LOGIN_TO_DISABLED_ACCOUNT_ERRORS = (By.CSS_SELECTOR, ".alert.alert-danger")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-of-type(1)")
