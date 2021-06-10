import pytest
import time
import math
from selenium import webdriver

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

answering_field_locator = ".quiz-component.ember-view"
submit_button_locator = ".submit-submission"
smart_hint_locator = ".smart-hints__hint"


def get_current_time_in_str_format():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="module")
def browser_for_message_puzzle():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.alieness
@pytest.mark.parametrize("link", links)
def test_feedback_for_message_parts(browser, link):
    browser.get(link)
    answer = get_current_time_in_str_format()
    answering_field = browser.find_element_by_tag_name("textarea")
    answering_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector(submit_button_locator)
    submit_button.click()
    smart_hint = browser.find_element_by_css_selector(smart_hint_locator)

    assert smart_hint.text == "Correct!", \
        f"Test for {link} has failed. The error looks like a part of a puzzle"
