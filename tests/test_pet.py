from helpers.pet_helper import PetHelper
from helpers.base_helper import setup_logging

logger = setup_logging()


# POST: Add a new pet to the store
def test_add_pet():
    pet_service = PetHelper("https://petstore.swagger.io/v2")
    new_pet_data = {
        "id": 123,
        "category": {"id": 123, "name": "maltipoo"},
        "name": "Benny",
        "photoUrls": ["https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image"
                      "-1652926025.jpg?crop=0.444xw:1.00xh;0.129xw,0&resize=980:*"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }

    logger.info(f"Adding a new pet with data: {new_pet_data}")

    added_pet_info = pet_service.add_pet(new_pet_data)

    logger.info(f"Received response: {added_pet_info}")

    if added_pet_info.status_code == 200:
        added_pet_info = added_pet_info.json()

        assert added_pet_info["name"] == new_pet_data[
            "name"], f"Expected pet name {new_pet_data['name']}, but got {added_pet_info['name']}"
        assert added_pet_info["status"] == new_pet_data[
            "status"], f"Expected pet status {new_pet_data['status']}, but got {added_pet_info['status']}"

    else:
        assert False, f"Expected status code 200, but got {added_pet_info.status_code}"


# GET: Find pet by ID
def test_get_pet_by_id():
    pet_service = PetHelper("https://petstore.swagger.io/v2")
    pet_id = 123

    logger.info(f"Getting a pet with ID: {pet_id}")

    pet_info = pet_service.get_pet_by_id(pet_id)

    logger.info(f"Received response: {pet_info}")

    if pet_info.status_code == 200:
        pet_info = pet_info.json()

        assert pet_info["id"] == pet_id, f"Expected pet ID {pet_id}, but got {pet_info['id']}"

    else:
        assert False, f"Expected status code 200, but got {pet_info.status_code}"


# POST: Upload an image
def test_upload_image():
    pet_service = PetHelper("https://petstore.swagger.io/v2")
    pet_id = 1
    image_path = "/Users/macbook/PycharmProjects/Prikhodko/API-autotests/image.jpeg"

    logger.info(f"Uploading the image for pet ID: {pet_id}")

    uploaded_image_info = pet_service.upload_image(pet_id, image_path)

    logger.info(f"Received response: {uploaded_image_info}")

    if uploaded_image_info.status_code == 200:
        uploaded_image_info = uploaded_image_info.json()

        assert "message" in uploaded_image_info, "Image upload failed"

    else:
        assert False, f"Expected status code 200, but got {uploaded_image_info.status_code}"


# PUT: Update an existing pet
def test_update_pet():
    pet_service = PetHelper("https://petstore.swagger.io/v2")
    updated_pet_data = {
        "id": 123,
        "name": "New Pet Name",
        "status": "sold"
    }

    logger.info(f"Updating pet with data: {updated_pet_data}")

    updated_pet_info = pet_service.update_pet(updated_pet_data)

    logger.info(f"Received response: {updated_pet_info}")

    if updated_pet_info.status_code == 200:
        updated_pet_info = updated_pet_info.json()

        assert updated_pet_info["name"] == updated_pet_data[
            "name"], f"Expected pet name {updated_pet_data['name']}, but got {updated_pet_info['name']}"
        assert updated_pet_info["status"] == updated_pet_data[
            "status"], f"Expected pet status {updated_pet_data['status']}, but got {updated_pet_info['status']}"

    else:
        assert False, f"Expected status code 200, but got {updated_pet_info.status_code}"
