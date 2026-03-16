import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL
from locators import MainPageLocators


class TestConstructor:

    def test_navigate_to_buns(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()

        assert wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_HEADING)
        ).is_displayed()

    def test_navigate_to_sauces(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()

        assert wait.until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_HEADING)
        ).is_displayed()

    def test_navigate_to_fillings(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()

        assert wait.until(
            EC.visibility_of_element_located(MainPageLocators.FILLINGS_HEADING)
        ).is_displayed()