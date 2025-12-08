from helpers.generator import random_string
import allure


@allure.suite("Логин курьера")
class TestLoginCourier:

    @allure.step("Успешный логин курьера")
    def test_login_success(self, courier_api, courier_data):
        courier_api.create(courier_data)

        response = courier_api.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })

        assert response.status_code == 200
        courier_id = response.json().get("id")

        courier_api.delete(courier_id)

    @allure.step("Логин курьера с неправильным паролем")
    def test_login_wrong_password(self, courier_api, courier_data):
        courier_api.create(courier_data)

        response = courier_api.login({
            "login": courier_data["login"],
            "password": "wrong"
        })

        assert response.status_code == 404

        login_resp = courier_api.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_api.delete(login_resp.json().get("id"))

    @allure.step("Логин без обязательного поля")
    def test_login_without_required_field(self, courier_api):
        response = courier_api.login({"login": "test"})
        assert response.status_code in [400, 504]

    @allure.step("Логин несуществующего курьера")
    def test_login_non_existing_user(self, courier_api):
        response = courier_api.login({
            "login": random_string(),
            "password": random_string()
        })
        assert response.status_code == 404
