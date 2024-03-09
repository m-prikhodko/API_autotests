from api.user_api import UserAPI


class TestUser:
    user_service = UserAPI()

    # POST: Creates list of users with given input array
    def test_create_users_with_array(self):
        user_service = UserAPI()
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

        new_users = user_service.create_users_with_array(users).json()

        assert new_users["message"] == "ok", f"Expected message is ok, but got {new_users['message']}"

    # PUT: Updated user
    def test_update_user(self):
        user_service = UserAPI()
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

        updated_user_info = user_service.update_user(user_name, update_user_data).json()

        assert updated_user_info["code"] == 200, f"Expected code is 200, but got {updated_user_info['code']}"
        assert updated_user_info["message"] == str(update_user_data[
                                                       "id"]), f"Expected message {update_user_data['id']}, but got {updated_user_info['status']}"
