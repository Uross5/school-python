import pymysql

from src.core.database import connect_to_db


def insert_payment(user_id, amount, created_at):
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        query = "INSERT INTO payments (user_id, amount, created_at) VALUES (%s,%s,%s)"
        cursor.execute(query, (user_id, amount, created_at))
        connection.commit()
    except pymysql.err.IntegrityError:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

def get_all_payments():
    connection = connect_to_db()
    cursor = connection.cursor()
    query="SELECT * FROM payments"
    cursor.execute(query)
    payments = cursor.fetchall()
    cursor.close()
    connection.close()
    return payments