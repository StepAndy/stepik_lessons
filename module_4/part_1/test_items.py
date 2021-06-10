from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

localized_button_text = {'ru': 'Добавить в корзину',
                         'en-GB': 'Add to basket',
                         'fr': 'Ajouter au panier',
                         'es': 'Añadir al carrito'}

button_locator = (By.CLASS_NAME, 'btn-add-to-basket')


def test_button_text_is_correct(browser, language):
    browser.get(link)

    add_to_basket_button = browser.find_element(*button_locator)
    button_text = add_to_basket_button.text

    assert button_text == localized_button_text[language], \
        f"Button's text must be '{localized_button_text[language]}'" \
        f", but text is '{button_text}'"
