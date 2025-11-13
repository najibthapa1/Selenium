# base/base_page.py
from selenium.webdriver.common.by import By
from base.base_element import BaseElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element(self, by, selector, name=""):
        return BaseElement(self.driver, (by, selector), name)