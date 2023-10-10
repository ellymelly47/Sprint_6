from selenium.webdriver.common.by import By


class OrderPageLocators:
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'  # кнопка "Далее"

    INPUT_NAME = By.XPATH, '//input[@placeholder="* Имя"]'  # инпут "Имя"
    INPUT_SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'  # инпут "Фамилия"
    INPUT_ADDRESS = By.XPATH, '//input[contains(@placeholder,"Адрес")]'  # инпут "Адрес.."

    INPUT_METRO = By.CLASS_NAME, 'select-search__input'  # инпут "Станция метро"

    SELECT_METRO = By.CLASS_NAME, 'select-search__options'  # выпадающий список станций метро

    METRO_OPTION_START_OF_LIST = By.XPATH, '//li[@data-index="3"]'  # станция "Сокольники" в списке

    METRO_OPTION_END_OF_LIST = By.XPATH, '//li[@data-index="216"]'  # станция "Деловой центр" в списке

    INPUT_PHONE = By.XPATH, '//input[contains(@placeholder,"Телефон")]'  # инпут "Телефон.."

    INPUT_DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  # инпут "Когда привезти самокат"
    CALENDAR = By.CLASS_NAME, 'react-datepicker'  # календарь

    CALENDAR_NEXT_MONTH_BUTTON = By.XPATH, '//button[contains(@class,"navigation--next")]'
    # кнопка перехода к след. месяцу в календаре
    CALENDAR_DATE_TODAY = By.XPATH, '//div[contains(@class,"today")]'
    # выделенная по умолчанию дата текущего месяца ("сегодня")
    CALENDAR_DATE_SELECTED = By.XPATH, '//*[contains(@class,"selected") and not(contains(@class, "outside-month"))]'
    # выделенная по умолчанию дата следующего месяца

    DROPDOWN_RENTAL_PERIOD = By.CLASS_NAME, 'Dropdown-control'  # поле "Срок аренды"

    RENTAL_PERIOD_DROPDOWN_MENU = By.CLASS_NAME, 'Dropdown-menu'  # выпадающий список Срока аренды

    RENTAL_PERIOD_MIN = By.XPATH, '//div[text()="сутки"]'  # срок аренды "сутки"
    RENTAL_PERIOD_MAX = By.XPATH, '//div[text()="семеро суток"]'  # срок аренды "семеро суток"

    COLOR_CHECKBOX_BLACK = By.ID, 'black'  # чекбокс цвета самоката "чёрный жемчуг"

    INPUT_COMMENT = By.XPATH, '//input[contains(@placeholder,"Комментарий")]'  # инпут "Комментарий.."

    ORDER_BUTTON = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'  # кнопка "Заказать"

    ORDER_YES_BUTTON = By.XPATH, '//button[text()="Да"]'  # кнопка "Да" во всплывающем окне подтверждения заказа

    ORDER_CONFIRM_TITLE = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    # заголовок "Хотите оформить заказ?" во всплывающем окне подтверждения заказа

    CHECK_STATUS_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'
    # кнопка "Посмотреть статус" в окне успешного заказа

    ORDER_SUCCESS_TITLE = By.XPATH, '//div[text()="Заказ оформлен"]'
    # заголовок "Заказ оформлен" в окне успешного заказа
