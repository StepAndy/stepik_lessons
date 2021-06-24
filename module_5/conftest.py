import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: en-GB, fr, es, ru")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--screenshots', action='store', default=False,
                     help="Takes screenshots. Usage: True/False")


@pytest.fixture()
def language(request):
    return str(request.config.getoption("--language"))


@pytest.fixture()
def browser(language, request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    screenshots = request.config.getoption("screenshots")
    if screenshots:
        # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
        browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()
