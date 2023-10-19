from selenium.webdriver.common.by import By


class HeaderLocators:
    YANDEX_LOGO = By.XPATH, '//*[@href="//yandex.ru"]'  # логотип "Яндекс" в хедере
    SCOOTER_LOGO = By.XPATH, '//*[@href="/"]'  # логотип "Самокат" в хедере

    HEADER_ORDER_BUTTON = By.XPATH, '//*[contains(@class,"Header_Nav")]//button[text()="Заказать"]'  # кнопка "Заказать" в хедере
