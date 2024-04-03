
from src.DAO.connectDAO import ConnectDAO
import random

class UserHelperDB(object):
    def __init__(self):
        self.execute = ConnectDAO()

    def get_random_email_from_DB(self, qty=1):

        sql = f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"
        exec_db = self.execute.execute_SELECT(sql)

        return random.sample(exec_db, qty)
