import requests
import allure
from conftest import *
from data import BASE_URL, COURIER_CREATE, SUCCESSFUL_CREATION_MESSAGE, DUPLICATE_COURIER_MESSAGE, MISSING_FIELD_MESSAGE

@allure.feature("Courier Management")
class TestCreateCourier:
    @allure.title("Create classic courier")
    def test_create_courier(self, create_courier, unique_courier):
        response = create_courier(unique_courier)
        assert response.status_code == 201
        assert response.json() == SUCCESSFUL_CREATION_MESSAGE

    @allure.title("Create duplicate courier")
    def test_create_duplicate_courier(self, create_courier, unique_courier):
        create_courier(unique_courier)
        response = create_courier(unique_courier)
        assert response.status_code == 409
        assert response.json().get("message") == DUPLICATE_COURIER_MESSAGE

    @pytest.mark.parametrize("missing_fields", [
        (["password", "firstName"]),
        (["login", "firstName"]),
        (["login", "password"])
    ])
    def test_create_courier_missing_field(self, unique_courier, missing_fields):
        courier_payload = unique_courier.copy()
        for field in missing_fields:
            courier_payload[field] = ""
        response = requests.post(f"{BASE_URL}{COURIER_CREATE}", json=courier_payload)
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        assert response.json().get("message") == MISSING_FIELD_MESSAGE, \
            f"Expected message '{MISSING_FIELD_MESSAGE}', got '{response.json().get('message')}'"






