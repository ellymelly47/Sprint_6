import allure
from data import user_1, user_2
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка успешного заказа: заполнение всех полей + минимальные значения параметров')
    def test_order_by_header_order_button(self, driver, agree_with_cookie):
        header_page = HeaderPage(driver)
        header_page.go_to_order_page_by_header_order_button()
        base_page = BasePage(driver)
        base_page.wait_until_element_visibility(3, OrderPageLocators.NEXT_BUTTON)

        order_page = OrderPage(driver)
        order_page.fill_name(user_1.name)
        order_page.fill_surame(user_1.surname)
        order_page.fill_address(user_1.address)
        order_page.focus_on_input_metro()
        base_page.wait_until_element_visibility(3, OrderPageLocators.SELECT_METRO)
        order_page.choose_metro_from_begining_of_list()
        order_page.fill_phone(user_1.phone)
        order_page.click_on_next_button()
        order_page.focus_on_input_date()
        base_page.wait_until_element_visibility(3, OrderPageLocators.CALENDAR)
        order_page.choose_date_today()
        order_page.focus_on_field_rental_period()
        base_page.wait_until_element_visibility(3, OrderPageLocators.RENTAL_PERIOD_DROPDOWN_MENU)
        order_page.choose_min_rental_period()
        order_page.choose_black_color()
        order_page.fill_comment(user_1.comment)
        order_page.submit_order()

        assert base_page.find_the_element(3, OrderPageLocators.ORDER_SUCCESS_TITLE).is_displayed(), \
            'Создание заказа завершилось ошибкой'

    @allure.title('Проверка успешного заказа: заполнение обязательных полей + максимальные значения параметров')
    def test_order_by_main_page_order_button(self, driver, agree_with_cookie):
        main_page = MainPage(driver)
        main_page.go_to_order_page_by_main_page_order_button()
        base_page = BasePage(driver)
        base_page.wait_until_element_visibility(3, OrderPageLocators.NEXT_BUTTON)

        order_page = OrderPage(driver)
        order_page.fill_name(user_2.name)
        order_page.fill_surame(user_2.surname)
        order_page.fill_address(user_2.address)
        order_page.focus_on_input_metro()
        base_page.wait_until_element_visibility(3, OrderPageLocators.SELECT_METRO)
        order_page.choose_metro_from_end_of_list()
        order_page.fill_phone(user_2.phone)
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
