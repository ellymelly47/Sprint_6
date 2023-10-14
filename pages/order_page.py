from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    def fill_surame(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    def fill_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    def focus_on_input_metro(self):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO).click()

    def choose_metro_from_begining_of_list(self):
        self.driver.find_element(*OrderPageLocators.METRO_OPTION_START_OF_LIST).click()

    def choose_metro_from_end_of_list(self):
        metro = self.driver.find_element(*OrderPageLocators.METRO_OPTION_END_OF_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", metro)
        self.driver.find_element(*OrderPageLocators.METRO_OPTION_END_OF_LIST).click()

    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def focus_on_input_date(self):
        self.driver.find_element(*OrderPageLocators.INPUT_DATE).click()

    def choose_date_today(self):
        self.driver.find_element(*OrderPageLocators.CALENDAR_DATE_TODAY).click()

    def choose_date_next_month(self):
        self.driver.find_element(*OrderPageLocators.CALENDAR_NEXT_MONTH_BUTTON).click()
        self.driver.find_element(*OrderPageLocators.CALENDAR_DATE_SELECTED).click()

    def focus_on_field_rental_period(self):
        self.driver.find_element(*OrderPageLocators.DROPDOWN_RENTAL_PERIOD).click()

    def choose_min_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_MIN).click()

    def choose_max_rental_period(self):
        max_period = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_MAX)
        self.driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", max_period)

    def choose_black_color(self):
        self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX_BLACK).click()

    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    def submit_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        self.click_on_element(3, OrderPageLocators.ORDER_YES_BUTTON)
