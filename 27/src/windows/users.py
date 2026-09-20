import tkinter as tk
from src.core.database import connect_to_db


def show_users_window(window):

    listbox = tk.Listbox(window)
    listbox.pack(side="left", fill="y")

    connection = connect_to_db()
    cursor = connection.cursor()
    query = "SELECT name FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    for user in users:
        listbox.insert(tk.END,user[0])

