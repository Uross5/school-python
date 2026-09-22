import tkinter as tk

from src.models.payment import get_all_payments


def show_payment_window(window):
    payments = get_all_payments()

    listbox = tk.Listbox(window)
    listbox.pack(side="left", fill="both", expand=True)
    for payment in payments:
        payment_id, user_id, amount, created_at = payment

        listbox.insert(tk.END, f"ID: {payment_id}, User ID: {user_id}, "
                               f"Amount: ${amount}, Date: {created_at.strftime('%d.%m.%Y')}"
                       )
