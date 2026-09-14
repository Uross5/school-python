import pymysql


class Db:
    def __init__(self):
        self.__connection=pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="oop_2",
        port=8888
    )

    def _get_connection(self):
        return self.__connection



