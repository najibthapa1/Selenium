# utils/data_provider.py
from faker import Faker

# Initialize Faker instance
fake = Faker()


def random_user():
    """
    Returns a dictionary with a random username and password
    Example:
        {
            "username": "john_doe123",
            "password": "P@ssw0rd!"
        }
    """
    return {
        "username": fake.user_name(),
        "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True)
    }


def random_email():
    """
    Generates a random email address
    """
    return fake.email()


def random_name():
    """
    Generates a random full name
    """
    return fake.name()


def random_phone():
    """
    Generates a random phone number
    """
    return fake.phone_number()


def random_address():
    """
    Generates a random address
    """
    return fake.address()