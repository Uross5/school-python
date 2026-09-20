import tkinter as tk


def show_users_window(window):

    users=["John","Michael","Lewis"]
    user_list=tk.Listbox(window)
    user_list.pack(side="left",fill="y")

    for user in users:
        user_list.insert(tk.END,user)