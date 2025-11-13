# pages/on_trade_customer.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class OnTradeCustomer(BasePage):
    @property
    def username(self):
        return self.element(By.ID, "username-input", "Username Field")

    @property
    def password(self):
        return self.element(By.ID, "password-input", "Password Field")

    @property
    def loginBtn(self):
        return self.element(By.CSS_SELECTOR, "button.login-btn", "Login Button")

    @property
    def toastMessage(self):
        return self.element(By.CSS_SELECTOR, "div.toast", "Toast Message")