import tkinter as tk
from src.components.navigation import show_navigation,switch_navigation_window
from src.components.body_frame import show_body_frame

def init():
    window=tk.Tk()
    window.geometry("500x500")
    window.title("Window")

    navigation=show_navigation(window)
    content=show_body_frame(window)
    navigation.bind("<<ListboxSelect>>", lambda event: switch_navigation_window(event, content))


    window.mainloop()

if __name__=="__main__":
    init()
