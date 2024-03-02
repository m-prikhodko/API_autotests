import requests


class StoreService:
    def __init__(self, base_url):
        self.base_url = base_url

    def place_order(self, order_data):
        url = f"{self.base_url}/store/order"
        response = requests.post(url, json=order_data)
        return response.json()

    def delete_order_by_id(self, order_id):
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.delete(url)
        return response.json()

    def get_order_by_id(self, order_id):
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.get(url)
        return response.json()




