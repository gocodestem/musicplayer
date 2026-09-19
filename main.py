'''
Initial Commit Version - 1.1 with Customtkinter
'''
import customtkinter as ctk
import MusicHandler
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, "Assets")

app = ctk.CTk()
app.geometry("800x800")
app.title("Zainify")
title = ctk.CTkLabel(app, text="Your collection").pack()

icon_path = os.path.join(base_dir, "Assets", "Logo.ico")
app.iconbitmap(icon_path)

app.mainloop()
