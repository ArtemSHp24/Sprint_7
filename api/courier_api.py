import requests
from config import BASE_URL


class CourierAPI:

    def create(self, body):
        return requests.post(f"{BASE_URL}/courier", json=body)

    def login(self, body):
        return requests.post(f"{BASE_URL}/courier/login", json=body)

    def delete(self, courier_id):
        return requests.delete(f"{BASE_URL}/courier/{courier_id}")
