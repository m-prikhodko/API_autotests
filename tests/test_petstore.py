from api.petstore_api import PetstoreAPI


class TestPetstore:
    store_service = PetstoreAPI()

    # POST: Place an order for a pet
    def test_place_order(self):
        new_order_data = {
            "id": 12345,
            "petId": 1,
            "quantity": 2,
            "shipDate": "2024-02-25T10:00:00Z",
            "status": "placed",
            "complete": False
        }

        placed_order_info = self.store_service.place_order(new_order_data).json()

        assert placed_order_info["id"] == new_order_data[
            "id"], f"Expected order id {new_order_data['id']}, but got {placed_order_info['id']}"
        assert placed_order_info["status"] == new_order_data[
            "status"], f"Expected order status {new_order_data['status']}, but got {placed_order_info['status']}"

    # GET: Find purchase order by ID
    def test_get_order_by_id(self):
        store_service = PetstoreAPI()
        order_id = 2

        order_info = store_service.get_order_by_id(order_id).json()

        assert order_info["id"] == order_id, f"Expected order ID {order_id}, but got {order_info['id']}"

    # DELETE: Delete order by ID
    def test_delete_order_by_id(self):
        store_service = PetstoreAPI()
        order_id = 12345

        order_info = store_service.delete_order_by_id(order_id).json()

        assert order_info["message"] == str(
            order_id), f"Expected deleted order ID {order_id}, but got {order_info['message']}"
        assert order_info["code"] == 200, f"Expected code 200, but got {order_info['code']}"
