import re
import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.geometry("700x400")

dark_mode=1

tk.Label(window,
         text="Hello how are you doing?",
         font=("Arial", 16),
         fg="darkblue",
         bg="orange"
         ).pack()
window.configure(bg="black")



def validate_password():
    user_password = password_entry.get()
    pattern = r"^123456$"
    if re.match(pattern, user_password):
        return True
    else:
        return False


def validate_email():
    user_email = email_entry.get()
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pattern, user_email):
        return True
    else:
        return False


def on_click():
    if validate_password() and validate_email():
        print("Welcome")
    else:
        print("Wrong email or password")


tk.Button(window,
          text="Sign up",
          font=("Arial", 16),
          fg="white",
          bg="blue",
          command=on_click
          ).pack(pady=20)

# ---------password entry-------
password_entry = tk.Entry(window, width=30)
password_entry.pack()

# -------email entry------

email_entry = tk.Entry(window, width=30)
email_entry.pack(pady=10)

#--------change mode-----------------

def change_mode():
    global dark_mode
    if dark_mode==0:
        window.configure(bg="black")
        dark_mode=1
    elif dark_mode==1:
        window.configure(bg="white")
        dark_mode=0

tk.Button(window,
          text="Dark mode",
          font=("Arial", 16),
          fg="white",
          bg="blue",
          command=change_mode
          ).pack(pady=20)



window.mainloop()
