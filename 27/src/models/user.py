import pymysql

from src.core.database import connect_to_db


def insert_user(username, email, dob):
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO users(name,email,dob) VALUES (%s,%s,%s)"
        cursor.execute(query, (username, email, dob))
        connection.commit()
    except pymysql.err.IntegrityError:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
