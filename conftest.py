from faker.proxy import Faker
import pytest


@pytest.fixture
def generate_random_phone_number():
    fake = Faker()
    phone_number = fake.random_int(min=1_000_000_000, max=9_999_999_999)
    return phone_number
