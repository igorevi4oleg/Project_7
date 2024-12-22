import requests
import allure
from conftest import *
from data import BASE_URL, COURIER_CREATE, SUCCESSFUL_CREATION_MESSAGE, DUPLICATE_COURIER_MESSAGE, \
    MISSING_FIELD_MESSAGE, ORDERS


@allure.feature("Order Management")
class TestCreateOrder:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.story("Create order with color options")
    def test_create_order(self, color):
        payload = {
            "firstName": "Evgenij",
            "lastName": "Volnov",
            "address": "Moscow, Pushkina str.",
            "metroStation": "4",
            "phone": "+7 915 256 25 26",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Dom Kalatushkina, kv. Petrova",
            "color": color
        }
        response = requests.post(f"{BASE_URL}{ORDERS}", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()