from pages.base_page import BasePage
from pages.header_page import HeaderPage
from locators.main_page_locators import MainPageLocators
from locators.yandex_page_locators import YandexSiteLocators


class TestHeaderPage:

    def test_redirect_by_scooter_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_site()
        base_page.go_to_order_page()

        header_page = HeaderPage(driver)
        header_page.click_on_scooter_logo()

        assert driver.find_element(*MainPageLocators.MAIN_PAGE_ORDER_BUTTON).is_displayed(), \
            'Не удалось перейти на главную страницу по клику на логотип "Самокат"'

    def test_redirect_by_yandex_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_site()

        header_page = HeaderPage(driver)
        header_page.click_on_yandex_logo()

        assert driver.find_element(*YandexSiteLocators.SEARCH_SUBMIT_BUTTON).is_displayed(), \
            'Не удалось перейти на главную страницу сайта Яндекс (Дзен)'
