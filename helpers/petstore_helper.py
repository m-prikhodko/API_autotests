import requests
from helpers.base_helper import BaseHelper


class PetstoreHelper(BaseHelper):

    def place_order(self, order_data):
        url = f"{self.base_url}/store/order"
        response = requests.post(url, json=order_data)
        return response

    def delete_order_by_id(self, order_id):
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.delete(url)
        return response

    def get_order_by_id(self, order_id):
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.get(url)
        return response
