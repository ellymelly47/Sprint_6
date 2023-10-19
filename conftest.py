from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def agree_with_cookie(driver):
    main_page = MainPage(driver)
    main_page.agree_with_cookie()
