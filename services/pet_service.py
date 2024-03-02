import requests


class PetService:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.post(url, json=pet_data)
        return response.json()

    def get_pet_by_id(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url)
        return response.json()

    def upload_image(self, pet_id, image_path):
        url = f"{self.base_url}/pet/{pet_id}/uploadImage"
        files = {"file": open(image_path, "rb")}
        response = requests.post(url, files=files)
        return response.json()

    def update_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        response = requests.put(url, json=pet_data)
        return response.json()
