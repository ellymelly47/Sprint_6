from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_question(self, num):
        method, locator = MainPageLocators.QUESTION_ACCORDION
        locator = locator.format(num)
        self.driver.find_element(method, locator).click()

    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_ACCORDION
        locator = locator.format(num)
        return self.driver.find_element(method, locator).text

    def go_to_order_page_by_main_page_order_button(self):
        self.driver.find_element(*MainPageLocators.MAIN_PAGE_ORDER_BUTTON).click()

    def agree_with_cookie(self):
        self.click_on_element(5, BasePageLocators.COOKIE_AGREE_BUTTON)
