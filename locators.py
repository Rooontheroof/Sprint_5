from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    BUNS_HEADING = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADING = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADING = (By.XPATH, "//h2[text()='Начинки']")


class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class RegisterPageLocators:

    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//form//fieldset[2]//input") 
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class ForgotPasswordPageLocators:

    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class ProfilePageLocators:

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")