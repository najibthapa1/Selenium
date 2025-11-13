# tests/test_customer_flow.py
import pytest
from selenium import webdriver
from base.dispatcher import Dispatcher
from pages.on_trade_customer import OnTradeCustomer
from utils.data_provider import random_user
from utils.env_utils import get_env


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(get_env("BASE_URL", "https://example.com/login"))
    yield driver
    driver.quit()


def test_customer_login(driver):
    page = OnTradeCustomer(driver)
    dispatcher = Dispatcher(page)

    user = random_user()

    steps = [
        {"sName": "username", "configs": [{"action": "setValue", "value": user["username"]}]},
        {"sName": "password", "configs": [{"action": "setValue", "value": user["password"]}]},
        {"sName": "loginBtn", "configs": [{"action": "click"}]},
        {"sName": "toastMessage", "configs": [{"action": "validateText", "value": "Login failed"}]},
    ]

    dispatcher.execute(steps)