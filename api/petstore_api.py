from api.base_request import BaseRequester


class PetstoreAPI(BaseRequester):

    def place_order(self, order_data):
        return self.send_request("POST", "/store/order", order_data)

    def delete_order_by_id(self, order_id):
        return self.send_request("DELETE", f"/store/order/{order_id}", order_id)

    def get_order_by_id(self, order_id):
        return self.send_request("GET", f"/store/order/{order_id}", order_id)
