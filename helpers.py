import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, LOGIN_URL, REGISTER_URL
from locators import RegisterPageLocators, LoginPageLocators


def generate_email():
    digits = "".join(random.choices(string.digits, k=3))
    return f"test_testov_{digits}@yandex.ru"


def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def register_and_get_credentials(driver):
    driver.get(REGISTER_URL)

    email = generate_email()
    password = generate_password()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)
    ).send_keys("Test User")

    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.url_to_be(LOGIN_URL)
    )

    return email, password


def register_and_login(driver):
    email, password = register_and_get_credentials(driver)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.url_to_be(BASE_URL + "/")
    )

    return email, password