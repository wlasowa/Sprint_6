import allure
from selenium.webdriver.common.keys import Keys

from locators import order_page_locators as order_loc
from pages.base_page import BasePageSamokat


class OrderPageSamokat(BasePageSamokat):
    @allure.step("Кликаем по логотипу Самоката")
    def click_samokat_logo(self):
        self.find_element(order_loc.SAMOKAT_LOGO).click()

    @allure.step("Заполняем данные клиента: {order_data}")
    def fill_customer_info(self, order_data):
        self.find_element(order_loc.NAME_FIELD).send_keys(order_data["name"])
        self.find_element(order_loc.SURNAME_FIELD).send_keys(order_data["surname"])
        self.find_element(order_loc.ADDRESS_FIELD).send_keys(order_data["address"])

        self.wait_clickable(order_loc.METRO_FIELD).send_keys(order_data["metro"])
        self.wait_clickable(
            self.format_locator(order_loc.METRO_LIST, order_data["metro"])
        ).click()

        self.find_element(order_loc.PHONE_FIELD).send_keys(order_data["phone"])

        self.find_element(order_loc.NEXT_PAGE_BTN).click()

    @allure.step("Заполняем данные аренды")
    def fill_rent_info(self, order_data):
        date_input = self.wait_clickable(order_loc.DATE_FIELD)
        date_input.send_keys(order_data["date"])
        date_input.send_keys(Keys.ENTER)

        self.wait_clickable(order_loc.PERIOD_LIST).click()
        self.wait_clickable(
            self.format_locator(order_loc.PERIOD_OPTION_LIST, order_data["period"])
        ).click()
        self.wait_clickable(
            self.format_locator(order_loc.COLOR_CHECKBOX, order_data["color"])
        ).click()

        self.find_element(order_loc.COMMENT_FIELD).send_keys(order_data["comment"])

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.wait_clickable(order_loc.ORDER_SUBMIT_BTN).click()
        self.wait_clickable(order_loc.ORDER_YES_BTN).click()

    @allure.step("Читаем текст окна завершения заказа")
    def get_order_finish_window_text(self):
        return self.wait_visible(order_loc.ORDER_FINISH_WINDOW).text
