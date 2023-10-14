from data import OrderName, OrderSurname, OrderAddress, OrderPhone, CommentToDriver
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    def test_order_by_header_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.agree_with_cookie()

        base_page = BasePage(driver)
        base_page.wait_until_element_invisibility(3, BasePageLocators.COOKIE_INFO_BLOCK)

        header_page = HeaderPage(driver)
        header_page.go_to_order_page_by_header_order_button()
        base_page.wait_until_element_visibility(3, OrderPageLocators.NEXT_BUTTON)

        order_page = OrderPage(driver)
        order_page.fill_name(OrderName.name_1)
        order_page.fill_surame(OrderSurname.surname_1)
        order_page.fill_address(OrderAddress.address_1)
        order_page.focus_on_input_metro()
        base_page.wait_until_element_visibility(3, OrderPageLocators.SELECT_METRO)
        order_page.choose_metro_from_begining_of_list()
        order_page.fill_phone(OrderPhone.phone_1)
        order_page.click_on_next_button()
        order_page.focus_on_input_date()
        base_page.wait_until_element_visibility(3, OrderPageLocators.CALENDAR)
        order_page.choose_date_today()
        order_page.focus_on_field_rental_period()
        base_page.wait_until_element_visibility(3, OrderPageLocators.RENTAL_PERIOD_DROPDOWN_MENU)
        order_page.choose_min_rental_period()
        order_page.choose_black_color()
        order_page.fill_comment(CommentToDriver.comment)
        order_page.submit_order()

        assert base_page.find_the_element(3, OrderPageLocators.ORDER_SUCCESS_TITLE).is_displayed(), \
            'Создание заказа завершилось ошибкой'

    def test_order_by_main_page_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.agree_with_cookie()

        base_page = BasePage(driver)
        base_page.wait_until_element_invisibility(3, BasePageLocators.COOKIE_INFO_BLOCK)
        main_page.go_to_order_page_by_main_page_order_button()
        base_page.wait_until_element_visibility(3, OrderPageLocators.NEXT_BUTTON)

        order_page = OrderPage(driver)
        order_page.fill_name(OrderName.name_2)
        order_page.fill_surame(OrderSurname.surname_2)
        order_page.fill_address(OrderAddress.address_2)
        order_page.focus_on_input_metro()
        base_page.wait_until_element_visibility(3, OrderPageLocators.SELECT_METRO)
        order_page.choose_metro_from_end_of_list()
        order_page.fill_phone(OrderPhone.phone_2)
        order_page.click_on_next_button()
        order_page.focus_on_input_date()
        base_page.wait_until_element_visibility(3, OrderPageLocators.CALENDAR)
        order_page.choose_date_next_month()
        order_page.focus_on_field_rental_period()
        base_page.wait_until_element_visibility(3, OrderPageLocators.RENTAL_PERIOD_DROPDOWN_MENU)
        order_page.choose_max_rental_period()
        order_page.submit_order()

        assert base_page.find_the_element(3, OrderPageLocators.ORDER_SUCCESS_TITLE).is_displayed(), \
            'Создание заказа завершилось ошибкой'
