from playwright.sync_api import TimeoutError

class LoginPage:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com"

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def verify_error_message(self, message):
        error = self.page.locator(self.ERROR_MESSAGE)
        error.wait_for(state="visible", timeout=3000)
        actual = error.inner_text().strip()
        assert actual == message, f"Expected '{message}', got '{actual}'"