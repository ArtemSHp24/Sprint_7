import pytest
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from helpers.generator import generate_courier


@pytest.fixture
def courier_api():
    return CourierAPI()


@pytest.fixture
def order_api():
    return OrderAPI()


@pytest.fixture
def courier_with_cleanup(courier_api):
   
    data = generate_courier()
    courier_api.create(data)

    yield data

    login_resp = courier_api.login({
        "login": data["login"],
        "password": data["password"]
    })

    courier_id = login_resp.json().get("id")

    if courier_id:
        courier_api.delete(courier_id)