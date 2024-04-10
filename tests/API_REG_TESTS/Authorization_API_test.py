import logging

from src.Helper.userHelperAPI import UserHelperAPI
from src.Utility.credentialsAPI import student_credentials
from src.Payload.payloads import Payloads
from src.Helper.userHelperDB import UserHelperDB

student_info = student_credentials()
random_user_payloads = Payloads().random_user_with_static_password()

import pytest
import allure
@pytest.mark.tcid13
def test_signin_as_student():
    result = UserHelperAPI().sign_in()
    with allure.step(f"The user: {result['user']['email']} is logged"):
        assert result["user"]["email"] == student_info['email'], f"Expected email result: {student_info['email']} \
                                                                         but API returned: {result['user']['email']}"

@pytest.mark.newuser
@pytest.mark.tcid11
def test_signup_as_student():
    message = "User was created"
    result = UserHelperAPI().create_user(random_user_payloads)

    email = {
        "email": random_user_payloads['email']
    }

    with allure.step(f"Expected message: {result['message']}"):
        assert result['message'] == message, f"Expected message: '{message}' but API returned: '{result['message']}'"
    return email

@pytest.mark.newuser
@pytest.mark.tcid12
def test_activate_user():
    email = test_signup_as_student().get('email')
    message = 'User was activated'
    exec_db = UserHelperDB().get_activation_code_from_DB(email)
    activ_code = exec_db[0]['activationCode']
    user_id = int(exec_db[0]['id'])
    exec_api = UserHelperAPI().activate_user(user_id, activ_code)
    logging.debug(exec_api['message'])
    with allure.step(f"User was activated"):
        assert exec_api['message'] == message, f"Expected message: '{message}' but API returned: '{exec_api['message']}'"













