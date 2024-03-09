import requests
from api.base_request import BaseRequester


class UserAPI(BaseRequester):

    def create_users_with_array(self, users):
        return self.send_request("POST", "/user/createWithArray", users)

    def update_user(self, user_name, user_data):
        return self.send_request("PUT", f"/user/{user_name}", user_data)

