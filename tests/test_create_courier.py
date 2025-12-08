import allure


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.step("Создание курьера — успешный случай")
    def test_create_courier_success(self, courier_api, courier_data):
        response = courier_api.create(courier_data)
        assert response.status_code == 201
        assert response.json().get("ok") is True

        login_response = courier_api.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json().get("id")
        courier_api.delete(courier_id)

    @allure.step("Создание двух одинаковых курьеров")
    def test_create_same_courier_twice(self, courier_api, courier_data):
        courier_api.create(courier_data)
        response = courier_api.create(courier_data)
        assert response.status_code == 409

        login_resp = courier_api.login({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_resp.json().get("id")
        courier_api.delete(courier_id)

    @allure.step("Создание курьера без обязательного поля")
    def test_create_courier_without_required_field(self, courier_api):
        body = {
            "password": "123",
            "firstName": "Test"
        }
        response = courier_api.create(body)
        assert response.status_code == 400
