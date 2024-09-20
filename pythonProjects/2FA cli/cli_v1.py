#library files
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

#variables
aspect_ratio=2/3

#functions
#function to maintain aspect ratio
def maintain_aspect_ratio(event):
    width = event.width
    height = event.height

    #calculate the desired height based on width
    desired_height=int(width/aspect_ratio)
    desired_width = int(height * aspect_ratio)

    # Adjust either width or height to maintain the aspect ratio
    if height != desired_height:
        # Adjust the height based on width
        win1.geometry(f"{width}x{desired_height}")
    elif width != desired_width:
        # Adjust the width based on height
        win1.geometry(f"{desired_width}x{height}")


#Adding new key
def add_key():
    win1.withdraw()

    #create new window instance
    win_add_key = tk.Tk()
    #set window title
    win_add_key.title("Add New Key")

    #set window size
    win_add_key.geometry("400x600")
    #maintain aspect ratio when resized
    win_add_key.bind("<Configure>", maintain_aspect_ratio)

    #set background colour
    win_add_key.config(bg="#272729")
    a = int(input("1/0"))
    if a==1:
        win_add_key.destroy()
        win1.deiconify()


#create main window
win1 = tk.Tk()

#set window title
win1.title("2FA by Ameer Salam")

#set window size
win1.geometry("400x600")
#maintain aspect ratio when resized
win1.bind("<Configure>", maintain_aspect_ratio)

icon = PhotoImage(file=f"icon_v1_nobg.png")
#set background colour
win1.config(bg="#121212")
win1.iconphoto(False, icon)



#MENUE BAR 
#create menu bar
menu_home = tk.Menu(win1)

menu_home.add_command(label="Add Key", command=add_key)
win1.config(menu=menu_home)

#start the tinkter loop
win1.mainloop()