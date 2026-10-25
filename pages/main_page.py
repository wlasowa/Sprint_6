import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from locators import main_page_locators as main_loc
from pages.base_page import BasePageSamokat


class MainPageSamokat(BasePageSamokat):
    @allure.step("Скроллим к вопросу FAQ №{num}")
    def scroll_to_question(self, num):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_clickable(self.format_locator(main_loc.FAQ_QUESTION, num))

    @allure.step("Кликаем по вопросу FAQ №{num}")
    def click_question(self, num):
        self.wait_clickable(self.format_locator(main_loc.FAQ_QUESTION, num)).click()

    @allure.step("Читаем текст ответа FAQ №{num}")
    def get_answer_text(self, num):
        return self.wait_visible(self.format_locator(main_loc.FAQ_ANSWER, num)).text

    @allure.step("Кликаем по кнопке заказа «{btn}»")
    def click_order_button(self, btn):
        if btn == "up":
            self.wait_clickable(main_loc.UP_ORDER_BTN).click()
        elif btn == "down":
            button = self.wait_present(main_loc.DOWN_ORDER_BTN)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", button
            )
            self.wait_clickable(main_loc.DOWN_ORDER_BTN).click()
        else:
            raise ValueError(f"Неизвестная кнопка заказа: {btn}")

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.wait_clickable(main_loc.YANDEX_LOGO).click()

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait_for(ec.url_to_be(urls.YA_URL))
