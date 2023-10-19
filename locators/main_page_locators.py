from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_ACCORDION = By.XPATH, '//*[@id="accordion__heading-{}"]'  # вопросы в блоке "Вопросы о важном"
    ANSWER_ACCORDION = By.XPATH, '//*[@id="accordion__panel-{}"]'  # ответы в блоке "Вопросы о важном"

    MAIN_PAGE_ORDER_BUTTON = By.XPATH, '//*[contains(@class,"FinishButton")]//button[text()="Заказать"]'
    # кнопка "Заказать" в середине страницы
