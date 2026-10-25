from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePageSamokat:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, *args):
        by, value = locator
        return by, value.format(*args)

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_present(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(locator)
        )

    def wait_for(self, condition):
        return WebDriverWait(self.driver, self.TIMEOUT).until(condition)
