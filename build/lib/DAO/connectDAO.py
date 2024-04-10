
from src.Utility.credentialsDB import credentialsDB

import pymysql.cursors

class ConnectDAO(object):
    def __init__(self):
        self.cred = credentialsDB()


    def connectDB(self):
        connection = pymysql.connect(
            user=self.cred['db_user'],
            password=self.cred['db_pass'],
            database=self.cred['db_name'],
            port=int(self.cred['db_port']),
            host=self.cred['db_host']
        )
        return connection


    def execute_SELECT(self, sql):
        conn = self.connectDB()

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

