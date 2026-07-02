import pytest
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # выбираем каким браузером открыть тест Chrome или Firefox
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # выбираем на каком языке проводить тест, по умолчанию eng
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en, es, fr, etc.')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference(
            'intl.accept_languages',
            user_language
        )

        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    print('\nquit browser..')
    browser.quit()

