import allure
import pytest

import urls
from data import ORDER_DATASET
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat


class TestOrderPageSamokat:
    @allure.title("Оформление заказа через кнопку «{btn}»")
    @allure.description(
        "Оформление заказа самоката: заполняем форму данными клиента и аренды, подтверждаем заказ и проверяем появление окна «Заказ оформлен»"
    )
    @pytest.mark.parametrize(
        "btn, data",
        [
            pytest.param("up", ORDER_DATASET[0], id="up_order_button_dataset_1"),
            pytest.param("down", ORDER_DATASET[1], id="down_order_button_dataset_2"),
        ],
    )
    def test_order_samokat(self, driver, btn, data):
        main_page = MainPageSamokat(driver)
        order_page = OrderPageSamokat(driver)

        main_page.click_order_button(btn)
        order_page.fill_customer_info(data)
        order_page.fill_rent_info(data)
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_order_finish_window_text()

    @allure.title("Переход на главную по логотипу Самоката")
    @allure.description(
        "Проверяем возврат на главную страницу при клике по логотипу Самоката со страницы оформления заказа"
    )
    def test_samokat_logo_open_main_page(self, driver):
        main_page = MainPageSamokat(driver)
        order_page = OrderPageSamokat(driver)

        main_page.click_order_button("up")
        order_page.click_samokat_logo()

        assert driver.current_url == urls.SAMOKAT_URL

    @allure.title("Переход на Яндекс по логотипу Яндекса")
    @allure.description(
        "Проверяем открытие сайта Яндекса в новой вкладке при клике по логотипу Яндекса"
    )
    def test_yandex_logo_open_ya(self, driver):
        main_page = MainPageSamokat(driver)

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert driver.current_url == urls.YA_URL
