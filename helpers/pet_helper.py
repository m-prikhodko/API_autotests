import requests
from helpers.base_helper import BaseHelper


class PetHelper(BaseHelper):

    def add_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.post(url, json=pet_data)
        return response

    def get_pet_by_id(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url)
        return response

    def upload_image(self, pet_id, image_path):
        url = f"{self.base_url}/pet/{pet_id}/uploadImage"
        files = {"file": open(image_path, "rb")}
        response = requests.post(url, files=files)
        return response

    def update_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.put(url, json=pet_data)
        return response
