from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL
from helpers import register_and_login
from locators import MainPageLocators, ProfilePageLocators


class TestPersonalAccount:

    def test_navigate_to_profile(self, driver):
        register_and_login(driver)

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        assert WebDriverWait(driver, 3).until(
            EC.url_contains("/account")
        )

    def test_navigate_to_constructor_via_link(self, driver):
        register_and_login(driver)

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)
        ).click()

        assert WebDriverWait(driver, 3).until(
            EC.url_to_be(BASE_URL + "/")
        )

    def test_navigate_to_constructor_via_logo(self, driver):
        register_and_login(driver)

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()

        assert WebDriverWait(driver, 3).until(
            EC.url_to_be(BASE_URL + "/")
        )

    def test_logout(self, driver):
        register_and_login(driver)

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 3).until(
            EC.url_contains("/login")
        )