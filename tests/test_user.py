from helpers.user_helper import UserHelper
from helpers.base_helper import setup_logging

logger = setup_logging()


# POST: Creates list of users with given input array
def test_create_users_with_array():
    user_service = UserHelper("https://petstore.swagger.io/v2")
    users = [
        {
            "id": 1,
            "username": "User1",
            "firstName": "Ben",
            "lastName": "Johnson",
            "email": "test@mail.ru",
            "password": "123456",
            "phone": "80294356783",
            "userStatus": 1
        },
        {
            "id": 2,
            "username": "User2",
            "firstName": "John",
            "lastName": "Doe",
            "email": "test2@mail.ru",
            "password": "987654",
            "phone": "80333456278",
            "userStatus": 1
        }
    ]

    logger.info(f"Creating users with array: {users}")

    new_users = user_service.create_users_with_array(users)

    logger.info(f"Received response: {new_users}")

    if new_users.status_code == 200:
        new_users = new_users.json()

        assert new_users["message"] == "ok", f"Expected message is ok, but got {new_users['message']}"

    else:
        assert False, f"Expected status code 200, but got {new_users.status_code}"


# PUT: Updated user
def test_update_user():
    user_service = UserHelper("https://petstore.swagger.io/v2")
    user_name = "User1"
    update_user_data = {
        "id": 123,
        "username": "User123",
        "firstName": "Ben",
        "lastName": "Johnson",
        "email": "test@mail.ru",
        "password": "123456",
        "phone": "80294356783",
        "userStatus": 1
    }

    logger.info(f"Updating user {user_name} with data: {update_user_data}")

    updated_user_info = user_service.update_user(user_name, update_user_data)

    logger.info(f"Received response: {updated_user_info}")

    if updated_user_info.status_code == 200:
        updated_user_info = updated_user_info.json()

        assert updated_user_info["code"] == 200, f"Expected code is 200, but got {updated_user_info['code']}"
        assert updated_user_info["message"] == str(update_user_data[
            "id"]), f"Expected message {update_user_data['id']}, but got {updated_user_info['status']}"

    else:
        assert False, f"Expected status code 200, but got {updated_user_info.status_code}"
