import requests
import allure
from config import BASE_URL


@allure.title("Get order list successefully")
class TestOrderList:
    def test_orders_list_get_success(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]


