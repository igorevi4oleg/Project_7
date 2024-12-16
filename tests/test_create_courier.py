from conftest import *
import requests
import pytest
import allure


@allure.title("Create courier with different options: classic, duplicate courier and with missing_field")
class TestCreateCourier:
    @allure.title("Create classic courier")
    def test_create_courier(self, courier_creation_teardown, unique_courier):
        response = courier_creation_teardown(unique_courier)
        assert response.status_code == 201, f"Unexpected response: {response.text}"
        assert response.json().get("ok") is True

    @allure.title("Create duplicate courier")
    def test_create_duplicate_courier(self, courier_creation_teardown, unique_courier):
        courier_creation_teardown(unique_courier)
        response = courier_creation_teardown(unique_courier)
        assert response.status_code == 409
        assert response.json().get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Create courier with missing_field")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, courier_creation_teardown, unique_courier, missing_field):
        courier_payload = unique_courier.copy()
        courier_payload.pop(missing_field)
        response = requests.post(f"{BASE_URL}/courier", json=courier_payload)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"





