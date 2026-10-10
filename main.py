'''
Initial Commit Version - 1.1 with Customtkinter
'''
import customtkinter as ctk
import MusicHandler
import os
from CTkTable import *

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, "Assets")
#first item is name, then artist, then album
testData = [
    ["Name","Artist","Album"],
    ["BigShot","ZainStuff","ZainStuff1"],
    ["Death By Glamour","ZainStuff","ZainStuff1"],
    ["Hammer Of Justice","ZainStuff","ZainStuff1"],
    ["It's Pizza","ZainStuff","ZainStuff1"],
    ["It's TV Time","ZainStuff","ZainStuff1"],
    ["BigShot2","ZainStuff","ZainStuff1"]
]



app = ctk.CTk()
app.geometry("800x800")
app.title("Zainify")
title = ctk.CTkLabel(app, text="Your collection").pack()

root = ctk.CTk()
table =  CTkTable(master=app, row = len(testData), column=len(testData[0]), values=testData,header_color="#00a2e8",text_color="#ffffff")
table.pack(expand=True, fill="both", padx=150, pady=20)

icon_path = os.path.join(base_dir, "Assets", "Logo.ico")
app.iconbitmap(icon_path)

app.mainloop()
