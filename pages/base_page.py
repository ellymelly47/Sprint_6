from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, sec: int, element_locator):
        element = WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))
        element.click()

    def find_the_element(self, sec: int, element_locator):
        element = WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))
        return element

    def wait_until_element_visibility(self, sec: int, element_locator):
        WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located(
            element_locator))

    def wait_until_element_invisibility(self, sec: int, element_locator):
        WebDriverWait(self.driver, sec).until(expected_conditions.invisibility_of_element_located(
            element_locator))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
