from selenium.webdriver.common.by import By


class YandexSiteLocators:
    SEARCH_SUBMIT_BUTTON = By.XPATH, '//button[text()="Найти"]'  # кнопка "Найти" на поисковой форме
