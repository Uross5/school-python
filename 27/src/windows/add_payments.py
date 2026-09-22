import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import pymysql

from src.models.payment import insert_payment


def save_payments(user_id_entry, amount_entry, created_at_entry):
    user_id = user_id_entry.get().strip()
    amount = amount_entry.get().strip()
    created_at = created_at_entry.get().strip()

    if user_id == "" or amount == "" or created_at == "":
        messagebox.showerror("Error", "All fields are required")
        return
    elif not user_id.isdigit():
        messagebox.showerror("Error", "User ID must be digits")
        return

    user_id = int(user_id)

    if (user_id) <= 0:
        messagebox.showerror("Error", "User ID must be greater than 0")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    try:
        created_at = datetime.strptime(created_at, "%d.%m.%Y").date()
    except ValueError:
        messagebox.showerror("Error", "Date must be in DD.MM.YYYY")
        return

    try:
        insert_payment(user_id, amount, created_at)
        user_id_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        created_at_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Payment has been added successfully")
    except pymysql.err.IntegrityError:
        messagebox.showerror("Error", "User with this ID does not exist")


def show_add_payments_window(window):
    tk.Label(window, text="User ID", font="Arial 16").pack()
    user_id = tk.Entry(window, font="Arial 16")
    user_id.pack(pady=5)

    tk.Label(window, text="Amount", font="Arial 16").pack()
    amount = tk.Entry(window, font="Arial 16")
    amount.pack(pady=5)

    tk.Label(window, text="Amount was added at: ", font="Arial 16").pack()
    created_at = tk.Entry(window, font="Arial 16")
    created_at.pack(pady=5)

    tk.Button(window, text="Deposit", font="Arial 16",
              command=lambda: save_payments(user_id, amount, created_at)).pack(pady=5)
