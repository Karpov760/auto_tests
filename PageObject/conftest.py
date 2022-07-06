import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "ru":
        print("\nstart ru browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        browser = webdriver.Chrome(options=options)
    elif language == "en":
        print("\nstart en browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print("\nstart browser for test..")

    yield browser
    print("\nquit browser..")
    browser.quit()