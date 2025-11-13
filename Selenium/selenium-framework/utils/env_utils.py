# utils/env_utils.py
import os

def get_env(key, default=None):
    return os.getenv(key, default)

# utils/data_provider.py
from faker import Faker
fake = Faker()

def random_user():
    return {
        "username": fake.user_name(),
        "password": fake.password(),
    }