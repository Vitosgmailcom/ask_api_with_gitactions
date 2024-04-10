import json

import allure
import requests
import logging as log

class Requests_API(object):
    def __init__(self):
        self.baseUrl = "http://ask-stage.portnov.com/api/v1/"

    def GET_request(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.baseUrl + endpoint
        with allure.step("Sent activation code"):
            req_call = requests.get(url=url, data=json.dumps(payload), headers=headers)
        response = requests.get(url)
        with allure.step(f"Status code:{response.status_code}"):
            assert response.status_code == int(expected_status_code), (f"Expected status code: {expected_status_code} but \""
                                                                   f"API returned: {req_call.status_code}")


        return response.json()

    def POST_request(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.baseUrl + endpoint

        req_call = requests.post(url=url, data=json.dumps(payload), headers=headers)
        with allure.step(f"Status code:{req_call.status_code}"):
            assert req_call.status_code == int(expected_status_code), (f"Expected status code: {expected_status_code} but \""
                                                                                   f"API returned: {req_call.status_code}")

        return req_call.json()


    def DELETE_request(self):
        pass