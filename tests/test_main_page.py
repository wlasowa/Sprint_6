import allure
import pytest

import data
from pages.main_page import MainPageSamokat


class TestMainPageSamokat:
    @allure.title("Проверка раскрытия вопросов FAQ и текстов ответа")
    @allure.description(
        "Проверяем FAQ на главной странице - кликаем на все вопросы и проверяем ответ"
    )
    @pytest.mark.parametrize(
        "num, expected_text",
        [
            pytest.param(num, text, id=f"question_{num + 1}")
            for num, text in data.FAQ_DATA
        ],
    )
    def test_faq(self, driver, num, expected_text):
        main_page = MainPageSamokat(driver)

        main_page.scroll_to_question(num)
        main_page.click_question(num)

        assert expected_text in main_page.get_answer_text(num)
