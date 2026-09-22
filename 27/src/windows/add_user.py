import re
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import pymysql

from src.models.user import insert_user


def validate_required_fields(username, email, dob):
    username = username.strip()
    email = email.strip()
    dob = dob.strip()

    if username == "" or email == "" or dob == "":
        raise ValueError("All fields are required")


def validate_username(username):
    username = username.strip()
    if sum(character.isalpha() for character in username) < 2:
        raise ValueError("Username must contain at least 2 letters")
    return username


def validate_email(email):
    email = email.strip()
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        raise ValueError("Email address is not valid")
    return email


def validate_dob(dob):
    dob = dob.strip()

    try:
        dob = datetime.strptime(dob, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("Date must be in the format DD.MM.YYYY")

    if dob > datetime.now().date():
        raise ValueError("Date cannot be in the future")

    return dob


def clear_user_fields(username_entry, email_entry, dob_entry):
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)


def save_user(username_entry, email_entry, dob_entry):
    username = username_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()

    try:
        validate_required_fields(username, email, dob)
        username = validate_username(username)
        email = validate_email(email)
        dob = validate_dob(dob)
    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return

    try:
        insert_user(username, email, dob)
        clear_user_fields(username_entry, email_entry, dob_entry)
        messagebox.showinfo("Success", "User has been added")
    except pymysql.err.IntegrityError:
        messagebox.showerror("Error", "User has not been added")


def show_add_user_window(window):
    tk.Label(window, text="Username", font="Arial 16").pack()
    username_entry = tk.Entry(window, font="Arial 16")
    username_entry.pack(pady=5)

    tk.Label(window, text="Email", font="Arial 16").pack()
    email_entry = tk.Entry(window, font="Arial 16")
    email_entry.pack(pady=5)

    tk.Label(window, text="Date of birth", font="Arial 16").pack()
    dob_entry = tk.Entry(window, font="Arial 16")
    dob_entry.pack(pady=5)

    tk.Button(window, text="Add User", font="Arial 16",
              command=lambda: save_user(username_entry, email_entry, dob_entry)).pack(pady=5)
