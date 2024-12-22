import requests
import allure
from conftest import *
from data import BASE_URL, GET_ORDERS

@allure.feature("Order Management")
class TestGetOrderList:
    def test_orders_list_get_success(self):
        response = requests.get(f"{BASE_URL}{GET_ORDERS}")
        assert type(response.json()["orders"]) == list and 'id' in response.json()["orders"][0]



