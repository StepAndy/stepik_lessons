from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class MainPageLocators:
    pass


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
    EMPTY_BASKET_INVALID = (By.CSS_SELECTOR, "wrong_ _")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
    PROCEED_TO_CHECKOUT_INVALID = (By.CSS_SELECTOR, ".content p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-of-type(1)")
