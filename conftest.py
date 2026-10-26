import pytest
from selenium import webdriver

import urls


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(urls.SAMOKAT_URL)
    yield browser
    browser.quit()
