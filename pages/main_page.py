from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            OrderPageLocators.NEXT_BUTTON))