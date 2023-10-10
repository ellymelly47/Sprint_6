from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.QUESTIONS_TITLE))

        self.driver.find_element(*BasePageLocators.COOKIE_AGREE_BUTTON).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(
            BasePageLocators.COOKIE_INFO_BLOCK))

    def go_to_order_page(self):
        self.driver.find_element(*HeaderLocators.HEADER_ORDER_BUTTON).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            OrderPageLocators.NEXT_BUTTON))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
