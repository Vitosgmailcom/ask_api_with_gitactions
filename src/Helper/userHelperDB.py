
from src.DAO.connectDAO import ConnectDAO
import random
import allure
class UserHelperDB(object):
    def __init__(self):
        with allure.step("Connect to DB"):
            self.execute = ConnectDAO()

    @property
    def get_random_email_from_DB(self, qty=1):
        with allure.step("Execute SELECT"):
            sql = f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"
            exec_db = self.execute.execute_SELECT(sql)

            return random.sample(exec_db, qty)

    def get_activation_code_from_DB(self, email):
        with allure.step("Retrieve activation code from DB"):
            sql = f"SELECT * FROM users WHERE `email`='{email}';"
            return self.execute.execute_SELECT(sql)


