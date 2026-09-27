
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MY_ACCOUNT)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_LINK)
        ).click()

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_warning_message(self):
        warning = self.wait.until(
            EC.visibility_of_element_located(self.WARNING_MESSAGE)
        )
        return warning.text

