import pytest
import requests
from helpers import generate_random_string
from data import BASE_URL, COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE

@pytest.fixture
def unique_courier():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }

@pytest.fixture
def create_courier():
    def create(payload):
        response = requests.post(f"{BASE_URL}{COURIER_CREATE}", json=payload)
        return response
    return create

@pytest.fixture
def delete_courier():
    def delete(courier_id):
        response = requests.delete(f"{BASE_URL}{COURIER_DELETE.format(courier_id=courier_id)}")
        return response
    return delete