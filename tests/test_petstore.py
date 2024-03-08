from helpers.petstore_helper import PetstoreHelper
from helpers.base_helper import setup_logging

logger = setup_logging()


# POST: Place an order for a pet
def test_place_order():
    store_service = PetstoreHelper("https://petstore.swagger.io/v2")
    new_order_data = {
        "id": 12345,
        "petId": 1,
        "quantity": 2,
        "shipDate": "2024-02-25T10:00:00Z",
        "status": "placed",
        "complete": False
    }

    logger.info(f"Placing order with data: {new_order_data}")

    placed_order_info = store_service.place_order(new_order_data)

    logger.info(f"Received response: {placed_order_info}")

    if placed_order_info.status_code == 200:
        placed_order_info = placed_order_info.json()

        assert placed_order_info["id"] == new_order_data[
            "id"], f"Expected order id {new_order_data['id']}, but got {placed_order_info['id']}"
        assert placed_order_info["status"] == new_order_data[
            "status"], f"Expected order status {new_order_data['status']}, but got {placed_order_info['status']}"

    else:
        assert False, f"Expected status code 200, but got {placed_order_info.status_code}"


# GET: Find purchase order by ID
def test_get_order_by_id():
    store_service = PetstoreHelper("https://petstore.swagger.io/v2")
    order_id = 2

    logger.info(f"Getting order by ID: {order_id}")

    order_info = store_service.get_order_by_id(order_id)

    logger.info(f"Received response: {order_info}")

    if order_info.status_code == 200:
        order_info = order_info.json()

        assert order_info["id"] == order_id, f"Expected order ID {order_id}, but got {order_info['id']}"

    else:
        assert False, f"Expected status code 200, but got {order_info.status_code}"


# DELETE: Delete order by ID
def test_delete_order_by_id():
    store_service = PetstoreHelper("https://petstore.swagger.io/v2")
    order_id = 12345

    logger.info(f"Deleting order by ID: {order_id}")

    order_info = store_service.delete_order_by_id(order_id)

    logger.info(f"Received response: {order_info}")

    if order_info.status_code == 200:
        order_info = order_info.json()

        assert order_info["message"] == str(
            order_id), f"Expected deleted order ID {order_id}, but got {order_info['message']}"
        assert order_info["code"] == 200, f"Expected code 200, but got {order_info['code']}"

    else:
        assert False, f"Expected status code 200, but got {order_info.status_code}"
