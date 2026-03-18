from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from helpers import register_and_get_credentials
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators
)


class TestLogin:

    def test_login_via_main_button(self, driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert wait.until(EC.url_to_be(BASE_URL + "/"))


    def test_login_via_personal_account_link(self, driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert wait.until(EC.url_to_be(BASE_URL + "/"))


    def test_login_via_register_page_link(self, driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_and_get_credentials(driver)

        driver.get(REGISTER_URL)

        wait.until(
            EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)
        ).click()

        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert wait.until(EC.url_to_be(BASE_URL + "/"))


    def test_login_via_forgot_password_link(self, driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_and_get_credentials(driver)

        driver.get(FORGOT_PASSWORD_URL)

        wait.until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        ).click()

        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert wait.until(EC.url_to_be(BASE_URL + "/"))
