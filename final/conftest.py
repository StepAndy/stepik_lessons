import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: en-GB, fr, es, ru")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    language = str(request.config.getoption("--language"))
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.FirefoxProfile()
        browser.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=browser)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
