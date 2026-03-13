from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from helpers import BASE_URL
from locators import MainPageLocators


class TestConstructor:

    def test_navigate_to_buns(self):
        """Переход к разделу «Булки» в конструкторе."""
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        # сначала переходим в другой раздел
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()

        # потом возвращаемся в Булки
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        ).click()

        heading = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNS_HEADING)
        )
        assert heading.is_displayed()

        driver.quit()

    def test_navigate_to_sauces(self):
        """Переход к разделу «Соусы» в конструкторе."""
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()

        heading = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES_HEADING)
        )
        assert heading.is_displayed()

        driver.quit()

    def test_navigate_to_fillings(self):
        """Переход к разделу «Начинки» в конструкторе."""
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        ).click()

        heading = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FILLINGS_HEADING)
        )
        assert heading.is_displayed()

        driver.quit()