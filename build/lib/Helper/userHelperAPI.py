from src.Utility.requests import Requests_API
from src.Utility.credentialsAPI import student_credentials
from src.Utility.credentialsAPI import teacher_credentials


import allure
import logging as log

class UserHelperAPI(object):
    def __init__(self):
        self.api_call = Requests_API()
        self.student_info = student_credentials()
        self.teacher_info = teacher_credentials()

    @allure.title("Creates new user with STUDENT permission and send verification email")
    def create_user(self, payload):
        return Requests_API().POST_request("sign-up", payload=payload, expected_status_code=200)


    @allure.title("Activates account after creation")
    def activate_user(self, userId, activationCode):
        req_call = Requests_API()
        return req_call.GET_request(f"activate/{userId}/{activationCode}", expected_status_code=200)


    @allure.title("Sign in user into application")
    def sign_in(self):
        return Requests_API().POST_request("sign-in", payload=self.student_info, expected_status_code=200)

    @allure.title("Submits request for password change")
    def forgot_password(self):
        pass

    @allure.title("Resets password after /forgot-password success")
    def reset_password(self):
        pass

