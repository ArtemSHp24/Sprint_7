import allure


@allure.suite("Получение списка заказов")
class TestGetOrdersList:

    @allure.step("Получение списка заказов")
    def test_get_orders_list(self, order_api):
        with allure.step("Отправляем запрос на получение списка заказов"):
            response = order_api.get_list()

        with allure.step("Проверяем 200 и что orders — список"):
            assert response.status_code == 200
            assert "orders" in response.json()
            assert isinstance(response.json()["orders"], list)
