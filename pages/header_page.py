import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Переходим на страницу заказа при клике на кнопку "Заказать" в хедере')
    def go_to_order_page_by_header_order_button(self):
        self.click_on_element(3, HeaderLocators.HEADER_ORDER_BUTTON)

    @allure.step('Переходим на главную страницу при клике на логотип Самокат в хедере')
    def click_on_scooter_logo(self):
        self.click_on_element(3, HeaderLocators.SCOOTER_LOGO)

    @allure.step('Переходим на главную стр. Яндекса в новой вкладке при клике на логотип Яндекс в хедере')
    def click_on_yandex_logo(self):
        self.click_on_element(3, HeaderLocators.YANDEX_LOGO)
        self.switch_to_new_window()
