import allure
from helpers.generator import generate_courier, random_string


@allure.suite("Логин курьера")
class TestLoginCourier:

    @allure.step("Успешный логин курьера")
    def test_login_success(self, courier_api, courier_with_cleanup):
        data = courier_with_cleanup

        response = courier_api.login({
            "login": data["login"],
            "password": data["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()


    @allure.step("Логин курьера с неправильным паролем")
    def test_login_wrong_password(self, courier_api, courier_with_cleanup):
        data = courier_with_cleanup

        response = courier_api.login({
            "login": data["login"],
            "password": "wrong"
        })

        assert response.status_code == 404


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
