import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import pymysql

from src.models.payment import insert_payment


def validate_required_fields(user_id, amount, created_at):
    user_id = user_id.strip()
    amount = amount.strip()
    created_at = created_at.strip()
    if user_id == "" or amount == "" or created_at == "":
        raise ValueError("All fields are required")


def validate_user_id(user_id):
    user_id = user_id.strip()
    if not user_id.isdigit():
        raise ValueError("User ID must be digits")
    user_id = int(user_id)
    if user_id <= 0:
        raise ValueError("User ID must be greater than 0")
    return user_id


def validate_amount(amount):
    amount = amount.strip()
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    return amount


def validate_created_at(created_at):
    created_at = created_at.strip()
    try:
        created_at = datetime.strptime(created_at, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("Date must be in DD.MM.YYYY")
    return created_at


def clear_payment_fields(user_id_entry, amount_entry, created_at_entry):
    user_id_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    created_at_entry.delete(0, tk.END)


def save_payments(user_id_entry, amount_entry, created_at_entry):
    user_id = user_id_entry.get()
    amount = amount_entry.get()
    created_at = created_at_entry.get()

    try:
        validate_required_fields(user_id, amount, created_at)
        user_id = validate_user_id(user_id)
        amount = validate_amount(amount)
        created_at = validate_created_at(created_at)
    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return

    try:
        insert_payment(user_id, amount, created_at)
        clear_payment_fields(user_id_entry, amount_entry, created_at_entry)
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
