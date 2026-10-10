'''
Initial Commit Version - 1.1 with Customtkinter
'''
import customtkinter as ctk
import MusicHandler
import os
from CTkTable import *
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))
filename1 = os.path.join(base_dir, "Assets")
filename2 = os.path.join(base_dir, "songlist.csv")
#first item is name, then artist, then album

#open the file DUMMY. Filename2 is the actual songlist csv, we found that out using base dir, which is just the musicplayer folder (lines 10-12)
with open(filename2, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    # convert it into a list
    testData = list(reader)

print(testData)

app = ctk.CTk()
app.geometry("800x800")
app.title("Zainify")
title = ctk.CTkLabel(app, text="Your collection").pack()

root = ctk.CTk()
table =  CTkTable(master=app, row = (len(testData) - 1), column=len(testData[0]), values=testData,header_color="#00a2e8",text_color="#ffffff")
table.pack(expand=True, fill="both", padx=150, pady=20)

icon_path = os.path.join(base_dir, "Assets", "Logo.ico")
app.iconbitmap(icon_path)

app.mainloop()
