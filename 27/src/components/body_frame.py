import tkinter as tk

def show_body_frame(window):
    content = tk.Frame(window,bg="white")
    content.pack(side="left",fill="both",expand=True)
    return content