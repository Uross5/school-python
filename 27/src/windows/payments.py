import tkinter as tk
from src.core.database import connect_to_db


def show_payment_window(window):
    connection = connect_to_db()
    cursor = connection.cursor()
    query="SELECT * FROM payments"
    cursor.execute(query)
    payments = cursor.fetchall()
    cursor.close()
    connection.close()

    listbox=tk.Listbox(window)
    listbox.pack(side="left",fill="both",expand=True)
    for payment in payments:
        payment_id, user_id, amount, created_at = payment

        listbox.insert(tk.END,f"ID: {payment_id}, User ID: {user_id}, "
            f"Amount: ${amount}, Date: {created_at.strftime('%d.%m.%Y')}"
        )