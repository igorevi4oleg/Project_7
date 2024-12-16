import pytest
import requests
import allure
from config import BASE_URL

@allure.title("Create order with different color options")
class TestCreateOrder:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
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
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()