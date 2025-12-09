import requests
from config import BASE_URL


class OrderAPI:

    def create(self, body):
        return requests.post(f"{BASE_URL}/orders", json=body)

    def get_list(self):
        return requests.get(f"{BASE_URL}/orders")
