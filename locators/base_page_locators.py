from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_INFO_BLOCK = By.XPATH, '//*[contains(@class,"CookieConsent")]'  # блок с информацией использование cookie
    COOKIE_AGREE_BUTTON = By.ID, 'rcc-confirm-button'  # кнопка подтверждения использования cookie
