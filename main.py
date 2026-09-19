'''
Initial Commit Version - 1.1 with Customtkinter
'''
import customtkinter as ctk
import MusicHandler

app = ctk.CTk()
app.geometry("800x800")
title = ctk.CTkLabel(app,text="Your collection").pack()

app.mainloop()