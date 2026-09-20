import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


def connect_to_db():
    connection = pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=int(os.environ["DB_PORT"])
    )

    return connection

