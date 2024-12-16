import pytest
import requests
import uuid
from config import BASE_URL

@pytest.fixture
def unique_courier():
    """Фикстура для генерации уникальных данных курьера."""
    return {
        "login": str(uuid.uuid4())[:10],
        "password": str(uuid.uuid4())[:10],
        "firstName": str(uuid.uuid4())[:10],
    }

@pytest.fixture
def get_courier_id():
    """Фикстура для получения ID курьера через логин."""
    def fetch_courier_id(courier_payload):
        login_response = requests.post(f"{BASE_URL}/courier/login", json=courier_payload)
        assert login_response.status_code == 200, f"Login failed: {login_response.text}"
        return login_response.json().get("id")
    return fetch_courier_id


@pytest.fixture
def courier_creation_teardown(get_courier_id):
    """Фикстура для создания и удаления курьеров."""
    created_couriers = []

    def register_courier(payload):
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        if response.status_code == 201:
            created_couriers.append(payload)
        return response

    yield register_courier

    # Удаляем созданных курьеров
    for courier_payload in created_couriers:
        courier_id = get_courier_id(courier_payload)
        if courier_id:
            delete_response = requests.delete(f"{BASE_URL}/courier/{courier_id}")
            if delete_response.status_code != 200:
                print(f"Failed to delete courier with id: {courier_id}, status code: {delete_response.status_code}")

    @pytest.fixture
    def create_and_login_courier():
        courier_payload = {
            "login": "test_courier",
            "password": "test_password",
            "firstName": "CourierName"
        }
        # Создаем курьера
        create_response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert create_response.status_code == 201
        courier_id = create_response.json().get("id")

        # Логинимся, чтобы убедиться, что курьер существует
        login_payload = {"login": "test_courier", "password": "test_password"}
        login_response = requests.post(f"{BASE_URL}/courier/login", json=login_payload)
        assert login_response.status_code == 200
        return courier_id