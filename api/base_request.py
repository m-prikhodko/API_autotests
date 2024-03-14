import logging
from http import HTTPStatus

import requests


class BaseRequester:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.base_url = self.BASE_URL
        self.logger = logging.getLogger(__name__)

    def send_request(self, method, endpoint, data=None, files=None, expected_status=HTTPStatus.OK):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, files=files)
        self.log_request_response(response)
        if response.status_code != expected_status:
            assert False, f"Unexpected status code: {response.status_code}"
        return response

    def log_request_response(self, response):
        request = response.request
        if request.method == "POST" or request.method == "PUT":
            body = request.body
            if len(body) > 1000:
                body = body[:1000]
        else:
            body = ""

        self.logger.info(
            f"Request method: {request.method}\n"
            f"Request url: {request.url}\n"
            f"Request body: {body}"
        )

        self.logger.info(
            f"Response status: {response.status_code}\n"
            f"Response data: {response.text}"
        )
