import allure
from conftest import *

@allure.title("Login courier: successful and unsuccessful")
class TestLoginCourier:
    @allure.title("Successful Login Courier")
    def test_login_successful(self, courier_creation_teardown, unique_courier):
        courier_creation_teardown(unique_courier)
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "login": unique_courier["login"],
            "password": unique_courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Unsuccessful login courier: with missing field")
    def test_login_missing_field(self, courier_creation_teardown, unique_courier, missing_field):
        courier_creation_teardown(unique_courier)
        login_data = {"login": unique_courier["login"], "password": unique_courier["password"]}
        login_data.pop(missing_field)
        print(f"Request payload: {login_data}")  # Отладка
        response = requests.post(f"{BASE_URL}/courier/login", json=login_data)
        print(f"Response: {response.status_code}, {response.text}")  # Отладка
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"