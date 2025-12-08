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
def courier_data():
    return generate_courier()
