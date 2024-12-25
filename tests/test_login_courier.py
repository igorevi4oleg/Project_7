import requests
import allure
from conftest import *
from data import BASE_URL, COURIER_LOGIN, MISSING_FIELD_LOGIN_MESSAGE

@allure.feature("Courier Management")
class TestLoginCourier:
    @allure.title("Successful login courier")
    def test_login_successful(self, create_courier, unique_courier):
        create_courier(unique_courier)
        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", json={
            "login": unique_courier["login"],
            "password": unique_courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Unsuccessful login courier: missing field")
    def test_login_missing_field(self, create_courier, unique_courier, missing_field):
        create_courier(unique_courier)
        login_data = {"login": unique_courier["login"], "password": unique_courier["password"]}
        login_data[missing_field] = ""
        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", json=login_data)
        assert response.status_code == 400
        assert response.json().get("message") == MISSING_FIELD_LOGIN_MESSAGE
