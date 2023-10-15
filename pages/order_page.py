import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем имя в инпуте "Имя"')
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step('Заполняем фамилию в инпуте "Фамилия"')
    def fill_surame(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем адрес в инпуте "Адрес.."')
    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Заполняем телефон в инпуте "Телефон.."')
    def fill_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step('Устанавливаем фокус в инпуте "Станция метро"')
    def focus_on_input_metro(self):
        self.click_on_element(3, OrderPageLocators.INPUT_METRO)

    @allure.step('Выбираем метро из первых станций выпадающего списка метро')
    def choose_metro_from_begining_of_list(self):
        self.click_on_element(3, OrderPageLocators.METRO_OPTION_START_OF_LIST)

    @allure.step('Выбираем метро из последних станций выпадающего списка метро (после скролла)')
    def choose_metro_from_end_of_list(self):
        metro = self.find_the_element(3, OrderPageLocators.METRO_OPTION_END_OF_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", metro)
        self.click_on_element(3, OrderPageLocators.METRO_OPTION_END_OF_LIST)

    @allure.step('Переходим ко второй части формы заказа кликом на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(3, OrderPageLocators.NEXT_BUTTON)

    @allure.step('Устанавливаем фокус в инпуте "Когда привезти самокат"')
    def focus_on_input_date(self):
        self.click_on_element(3, OrderPageLocators.INPUT_DATE)

    @allure.step('Выбираем дату для заказа: сегодня')
    def choose_date_today(self):
        self.click_on_element(3, OrderPageLocators.CALENDAR_DATE_TODAY)

    @allure.step('Выбираем дату для заказа: в следуюущем месяце')
    def choose_date_next_month(self):
        self.click_on_element(3, OrderPageLocators.CALENDAR_NEXT_MONTH_BUTTON)
        self.click_on_element(3, OrderPageLocators.CALENDAR_DATE_SELECTED)

    @allure.step('Кликаем на поле "Срок аренды"')
    def focus_on_field_rental_period(self):
        self.click_on_element(3, OrderPageLocators.DROPDOWN_RENTAL_PERIOD)

    @allure.step('Выбираем минимальный срок аренды: сутки')
    def choose_min_rental_period(self):
        self.click_on_element(3, OrderPageLocators.RENTAL_PERIOD_MIN)

    @allure.step('Выбираем максимальный срок аренды: семеро суток')
    def choose_max_rental_period(self):
        max_period = self.find_the_element(3, OrderPageLocators.RENTAL_PERIOD_MAX)
        self.driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", max_period)

    @allure.step('Выбираем цвет самоката: ставим галку в чекбоксе "черный жемчуг"')
    def choose_black_color(self):
        self.click_on_element(3, OrderPageLocators.COLOR_CHECKBOX_BLACK)

    @allure.step('Заполняем комментарий в инпуте "Комментарий для курьера"')
    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step('Подтверждаем оформление заказа кликом на кнопку "Заказать", и далее кликом на кнопку "Да"')
    def submit_order(self):
        self.click_on_element(3, OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(3, OrderPageLocators.ORDER_YES_BUTTON)
