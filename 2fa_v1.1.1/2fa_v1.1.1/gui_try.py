from asyncio.tasks import _CustomTaskConstructor
import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x300")

def list_of_2fa():
    print("Test!")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)