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

        wait.until(
            EC.text_to_be_present_in_element_attribute(
                MainPageLocators.BUNS_TAB,
                "class",
                "tab_tab_type_current"
            )
        )

        buns_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")


    def test_navigate_to_sauces(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()

        wait.until(
            EC.text_to_be_present_in_element_attribute(
                MainPageLocators.SAUCES_TAB,
                "class",
                "tab_tab_type_current"
            )
        )

        sauces_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.SAUCES_TAB))
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")


    def test_navigate_to_fillings(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()

        wait.until(
            EC.text_to_be_present_in_element_attribute(
                MainPageLocators.FILLINGS_TAB,
                "class",
                "tab_tab_type_current"
            )
        )
        
        fillings_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_TAB))
        assert "tab_tab_type_current" in fillings_tab.get_attribute("class")