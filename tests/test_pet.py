from api.pet_api import PetAPI


class TestPet:
    pet_service = PetAPI()

    # POST: Add a new pet to the store
    def test_add_pet(self):
        new_pet_data = {
            "id": 123,
            "category": {"id": 123, "name": "maltipoo"},
            "name": "Benny",
            "tags": [{"id": 1, "name": "friendly"}],
            "status": "available"
        }

        added_pet_info = self.pet_service.add_pet(new_pet_data).json()

        assert added_pet_info["name"] == new_pet_data[
            "name"], f"Expected pet name {new_pet_data['name']}, but got {added_pet_info['name']}"
        assert added_pet_info["status"] == new_pet_data[
            "status"], f"Expected pet status {new_pet_data['status']}, but got {added_pet_info['status']}"

        get_new_pet_info = self.pet_service.get_pet_by_id(new_pet_data['id']).json()
        assert get_new_pet_info['id'] == new_pet_data['id']

    # GET: Find pet by ID
    def test_get_pet_by_id(self):
        pet_id = 123

        pet_info = self.pet_service.get_pet_by_id(pet_id).json()

        assert pet_info["id"] == pet_id, f"Expected pet ID {pet_id}, but got {pet_info['id']}"

    # POST: Upload an image
    def test_upload_image(self):
        pet_id = 1
        image_path = "/Users/macbook/PycharmProjects/Prikhodko/API-autotests/image.jpeg"

        uploaded_image_info = self.pet_service.upload_image(pet_id, image_path).json()

        assert "message" in uploaded_image_info, "Image upload failed"

    # PUT: Update an existing pet
    def test_update_pet(self):
        updated_pet_data = {
            "id": 123,
            "name": "New Pet Name",
            "status": "sold"
        }

        updated_pet_info = self.pet_service.update_pet(updated_pet_data).json()

        assert updated_pet_info["name"] == updated_pet_data[
            "name"], f"Expected pet name {updated_pet_data['name']}, but got {updated_pet_info['name']}"
        assert updated_pet_info["status"] == updated_pet_data[
            "status"], f"Expected pet status {updated_pet_data['status']}, but got {updated_pet_info['status']}"
