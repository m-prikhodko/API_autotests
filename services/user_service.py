import requests


class UserService:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_users_with_array(self, users):
        url = f"{self.base_url}/user/createWithArray"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=users, headers=headers)
        return response.json()

    def update_user(self, user_name, user_data):
        url = f"{self.base_url}/user/{user_name}"
        response = requests.put(url, json=user_data)
        return response.json()
