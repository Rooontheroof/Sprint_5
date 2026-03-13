from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, PROFILE_URL, generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ProfilePageLocators


def register_and_login():
    email = generate_email()
    password = generate_password()

    driver = webdriver.Chrome()
    driver.get(REGISTER_URL)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)
    ).send_keys("Test User")

    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.url_to_be(LOGIN_URL)
    )

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.url_to_be(BASE_URL + "/")
    )

    return driver


class TestPersonalAccount:

    def test_navigate_to_profile(self):
        driver = register_and_login()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_contains("/account")
        )

        assert "/account" in driver.current_url
        driver.quit()

    def test_navigate_to_constructor_via_link(self):
        driver = register_and_login()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL + "/")
        )

        assert driver.current_url == BASE_URL + "/"
        driver.quit()

    def test_navigate_to_constructor_via_logo(self):
        driver = register_and_login()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL + "/")
        )

        assert driver.current_url == BASE_URL + "/"
        driver.quit()

    def test_logout(self):
        driver = register_and_login()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_contains("/login")
        )

        assert "/login" in driver.current_url
        driver.quit()