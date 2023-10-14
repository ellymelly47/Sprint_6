from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def go_to_order_page_by_header_order_button(self):
        self.driver.find_element(*HeaderLocators.HEADER_ORDER_BUTTON).click()

    def click_on_scooter_logo(self):
        self.driver.find_element(*HeaderLocators.SCOOTER_LOGO).click()

    def click_on_yandex_logo(self):
        self.driver.find_element(*HeaderLocators.YANDEX_LOGO).click()
        self.switch_to_new_window()
