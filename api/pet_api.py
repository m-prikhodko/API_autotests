from api.base_request import BaseRequester


class PetAPI(BaseRequester):

    def add_pet(self, pet_data):
        return self.send_request("POST", "/pet", pet_data)

    def get_pet_by_id(self, pet_id):
        return self.send_request("GET", f"/pet/{pet_id}")

    def upload_image(self, pet_id, image_path):
        files = {"file": open(image_path, "rb")}
        return self.send_request("POST", f"/pet/{pet_id}/uploadImage", files=files)

    def update_pet(self, pet_data):
        return self.send_request("PUT", "/pet", pet_data)
