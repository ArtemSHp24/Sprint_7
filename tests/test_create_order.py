import pytest
import allure


@allure.suite("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.step("Создание заказа с параметризацией цветов")
    def test_create_order(self, order_api, colors):
        body = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Street",
            "metroStation": 5,
            "phone": "+79999999999",
            "rentTime": 3,
            "deliveryDate": "2024-10-10",
            "comment": "test",
            "color": colors
        }

        response = order_api.create(body)
        assert response.status_code == 201
        assert response.json().get("track") is not None
