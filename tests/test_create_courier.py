import requests
import allure
from conftest import *
from data import BASE_URL, COURIER_CREATE, SUCCESSFUL_CREATION_MESSAGE, DUPLICATE_COURIER_MESSAGE, MISSING_FIELD_MESSAGE

@allure.feature("Courier Management")
class TestCreateCourier:
    @allure.story("Create classic courier")
    def test_create_courier(self, create_courier, unique_courier):
        response = create_courier(unique_courier)
        assert response.status_code == 201
        assert response.json() == SUCCESSFUL_CREATION_MESSAGE

    @allure.story("Create duplicate courier")
    def test_create_duplicate_courier(self, create_courier, unique_courier):
        create_courier(unique_courier)
        response = create_courier(unique_courier)
        assert response.status_code == 409
        assert response.json().get("message") == DUPLICATE_COURIER_MESSAGE

    @allure.story("Create courier with missing fields")
    def test_create_courier_missing_field(self, unique_courier):
        for missing_field in ["login", "password", "firstName"]:
            courier_payload = unique_courier.copy()
            courier_payload[missing_field] = ""
            response = requests.post(f"{BASE_URL}{COURIER_CREATE}", json=courier_payload)
            assert response.status_code == 400
            assert response.json().get("message") == MISSING_FIELD_MESSAGE






