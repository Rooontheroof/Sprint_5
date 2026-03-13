from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL, generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators


def register_and_get_credentials():
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
    driver.quit()
    return email, password


class TestLogin:

    def test_login_via_main_button(self):
        email, password = register_and_get_credentials()

        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL + "/")
        )
        assert driver.current_url == BASE_URL + "/"

        driver.quit()

    def test_login_via_personal_account_link(self):
        email, password = register_and_get_credentials()

        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

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
        assert driver.current_url == BASE_URL + "/"

        driver.quit()

    def test_login_via_register_page_link(self):
        email, password = register_and_get_credentials()

        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)
        ).click()

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
        assert driver.current_url == BASE_URL + "/"

        driver.quit()

    def test_login_via_forgot_password_link(self):
        email, password = register_and_get_credentials()

        driver = webdriver.Chrome()
        driver.get(FORGOT_PASSWORD_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        ).click()

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
        assert driver.current_url == BASE_URL + "/"

        driver.quit()
