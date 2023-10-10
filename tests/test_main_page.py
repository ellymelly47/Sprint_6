import pytest
from data import FaqAnswers
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, e_result',
        [(0, FaqAnswers.answer_0),
         (1, FaqAnswers.answer_1),
         (2, FaqAnswers.answer_2),
         (3, FaqAnswers.answer_3),
         (4, FaqAnswers.answer_4),
         (5, FaqAnswers.answer_5),
         (6, FaqAnswers.answer_6),
         (7, FaqAnswers.answer_7)]
    )
    def test_faq(self, driver, num, e_result):
        base_page = BasePage(driver)
        base_page.open_site()

        main_page = MainPage(driver)
        main_page.click_on_question(num)
        answer = main_page.get_answer(num)

        assert answer == e_result, 'Не удалось получить корректный ответ на вопрос'
