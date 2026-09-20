import tkinter as tk

def show_payment_window(window):
    payments=["John, 500, 11.11.2025","Steve, 1100, 03.12.2012","Steph, 5000,10.10.2021"]

    listbox=tk.Listbox(window)
    listbox.pack(side="left",fill="y")
    for payment in payments:
        listbox.insert(tk.END,payment)