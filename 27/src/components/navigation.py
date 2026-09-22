import tkinter as tk
from src.windows.users import show_users_window
from src.windows.payments import show_payment_window
from src.windows.add_user import show_add_user_window
from src.windows.add_payments import show_add_payments_window

def switch_navigation_window(event,content):
    listbox=event.widget
    selected_item=listbox.curselection()
    if not selected_item:
        return

    name=listbox.get(selected_item[0])

    for widget in content.winfo_children():
        widget.destroy()

    if name.lower()=="payments":
        show_payment_window(content)
    elif name.lower()=="users":
        show_users_window(content)
    elif name.lower()=="adding_user":
        show_add_user_window(content)
    elif name.lower()=="adding payments":
        show_add_payments_window(content)




def show_navigation (window):
    nav_item = ["payments", "users", "adding payments","adding_user"]

    navigation = tk.Listbox(window)
    navigation.pack(side="left",fill="y",padx=5)

    for item in nav_item:
        navigation.insert(tk.END, item)

    return navigation