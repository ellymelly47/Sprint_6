import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликаем поочередно на вопросы в блоке "Вопросы о важном"')
    def click_on_question(self, num):
        method, locator = MainPageLocators.QUESTION_ACCORDION
        locator = locator.format(num)
        self.click_on_element(3, (method, locator))

    @allure.step('Получаем поочередно тексты ответов на вопросы в блоке "Вопросы о важном"')
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_ACCORDION
        locator = locator.format(num)
        return self.get_text_from_element((method, locator))

    @allure.step('Переходим на страницу заказа при клике на кнопку "Заказать" на главной стр.')
    def go_to_order_page_by_main_page_order_button(self):
        self.click_on_element(3, MainPageLocators.MAIN_PAGE_ORDER_BUTTON)

    @allure.step('Скрываем всплывающий блок с информацией о cookie кликом на кнопку "да все привыкли"')
    def agree_with_cookie(self):
        self.click_on_element(5, BasePageLocators.COOKIE_AGREE_BUTTON)
        self.wait_until_element_invisibility(3, BasePageLocators.COOKIE_INFO_BLOCK)
