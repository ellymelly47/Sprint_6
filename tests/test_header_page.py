from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.yandex_page_locators import YandexSiteLocators
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.main_page import MainPage


class TestHeaderPage:

    def test_redirect_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.agree_with_cookie()

        base_page = BasePage(driver)
        base_page.wait_until_element_invisibility(3, BasePageLocators.COOKIE_INFO_BLOCK)

        header_page = HeaderPage(driver)
        header_page.go_to_order_page_by_header_order_button()
        base_page.wait_until_element_visibility(3, OrderPageLocators.NEXT_BUTTON)
        header_page.click_on_scooter_logo()

        assert base_page.find_the_element(3, MainPageLocators.MAIN_PAGE_ORDER_BUTTON).is_displayed(), \
            'Не удалось перейти на главную страницу по клику на логотип "Самокат"'

    def test_redirect_by_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.agree_with_cookie()

        base_page = BasePage(driver)
        base_page.wait_until_element_invisibility(3, BasePageLocators.COOKIE_INFO_BLOCK)

        header_page = HeaderPage(driver)
        header_page.click_on_yandex_logo()

        assert base_page.find_the_element(5, YandexSiteLocators.SEARCH_SUBMIT_BUTTON).is_displayed(), \
            'Не удалось перейти на главную страницу сайта Яндекс (Дзен)'
