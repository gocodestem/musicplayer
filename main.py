'''
Initial Commit Version - 1.1 with Customtkinter
'''
import customtkinter as ctk
import MusicHandler
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, "Assets")

testData = [
    {"Name":"BigShot","Artist":"ZainStuff","Album":"ZainStuff1"},
    {"Name":"Death By Glamour","Artist":"ZainStuff","Album":"ZainStuff1"},
    {"Name":"Hammer Of Justice","Artist":"ZainStuff","Album":"ZainStuff1"},
    {"Name":"It's Pizza","Artist":"ZainStuff","Album":"ZainStuff1"},
    {"Name":"It's TV Time","Artist":"ZainStuff","Album":"ZainStuff1"},
    {"Name":"BigShot2","Artist":"ZainStuff","Album":"ZainStuff1"}
]


app = ctk.CTk()
app.geometry("800x800")
app.title("Zainify")
title = ctk.CTkLabel(app, text="Your collection").pack()

icon_path = os.path.join(base_dir, "Assets", "Logo.ico")
app.iconbitmap(icon_path)

app.mainloop()
