import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import REGISTER_URL, LOGIN_URL, generate_email, generate_password
from locators import RegisterPageLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 10)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert wait.until(EC.url_to_be(LOGIN_URL))

    def test_registration_with_invalid_password(self, driver):
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 10)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        ).is_displayed()