
from src.Utility.randomData import random_email_and_password

class Payloads(object):
    def __init__(self):
        self.random_email = random_email_and_password()
    def random_user_with_static_password(self):
        payload = dict()
        payload['email'] = self.random_email['email']
        payload['name'] = "Will Smit"
        payload['password'] = 'Password1'
        payload['group'] = "APG999"
        return payload

    def teacher_user_password(self):
        pass


    def existing_student_email_password(self):
        pass
