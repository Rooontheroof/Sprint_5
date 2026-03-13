from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from helpers import REGISTER_URL, LOGIN_URL, generate_email, generate_password
from locators import RegisterPageLocators


class TestRegistration:

    def test_successful_registration(self):
        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        email = generate_email()
        password = generate_password()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)
        ).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )
        assert driver.current_url == LOGIN_URL

        driver.quit()

    def test_registration_with_invalid_password(self):
        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)
        ).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert error.is_displayed()

        driver.quit()
