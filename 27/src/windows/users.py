import tkinter as tk

from src.models.user import get_all_users


def show_users_window(window):
    listbox = tk.Listbox(window)
    listbox.pack(side="left", fill="y")

    users = get_all_users()

    for user in users:
        listbox.insert(tk.END, user[0].title())
