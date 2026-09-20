import tkinter as tk
from src.core.database import connect_to_db

def save_user(username,email,dob):
    connection = connect_to_db()
    cursor = connection.cursor()
    query="INSERT INTO users(name,email,dob) VALUES (%s,%s,%s)"
    cursor.execute(query,(username,email,dob))
    connection.commit()
    cursor.close()
    connection.close()
    print("user added")

def show_add_user_window(window):
    tk.Label(window,text="Username",font="Arial 16").pack()
    username_entry=tk.Entry(window,font="Arial 16")
    username_entry.pack(pady=5)

    tk.Label(window, text="Email", font="Arial 16").pack()
    email_entry = tk.Entry(window, font="Arial 16")
    email_entry.pack(pady=5)

    tk.Label(window, text="Date of birth", font="Arial 16").pack()
    dob_entry = tk.Entry(window, font="Arial 16")
    dob_entry.pack(pady=5)



    tk.Button(window,text="Add User", font="Arial 16",
              command=lambda: save_user(username_entry.get(),email_entry.get(),dob_entry.get()) ).pack(pady=5)

