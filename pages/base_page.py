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

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def switch_to_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait_for(ec.url_to_be(url))

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_into_view(self, element, block="center"):
        self.driver.execute_script(
            f"arguments[0].scrollIntoView({{block: '{block}'}});", element
        )
