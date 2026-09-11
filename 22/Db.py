import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
class Db:
    def __init__(self):
        self.connection=pymysql.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"],
            port=int(os.environ["DB_PORT"])
        )
db = Db()
print("Connected successfully")