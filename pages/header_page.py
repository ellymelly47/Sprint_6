from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.yandex_page_locators import YandexSiteLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_scooter_logo(self):
        self.driver.find_element(*HeaderLocators.SCOOTER_LOGO).click()

        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.QUESTIONS_TITLE))

    def click_on_yandex_logo(self):
        self.driver.find_element(*HeaderLocators.YANDEX_LOGO).click()

        self.switch_to_new_window()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            YandexSiteLocators.SEARCH_SUBMIT_BUTTON))
