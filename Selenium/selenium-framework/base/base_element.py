# base/base_element.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, locator: tuple, name: str = ""):
        self.driver = driver
        self.locator = locator
        self.name = name or str(locator)

    def find(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )

    def click(self):
        self.find().click()

    def set_value(self, value: str):
        el = self.find()
        el.clear()
        el.send_keys(value)

    def get_text(self):
        return self.find().text

    def validate_text(self, expected: str):
        actual = self.get_text()
        assert expected in actual, f"[{self.name}] Expected '{expected}' but got '{actual}'"