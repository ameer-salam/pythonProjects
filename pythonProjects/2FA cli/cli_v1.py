#library files
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
    win_add_key = tk.Toplevel()
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
icon_image = Image.open("icon_v1_nobg.png")  # Load the image with transparent background
icon_image = icon_image.resize((150, 150), Image.Resampling.LANCZOS)  # Use LANCZOS for resizing

# Convert the Pillow image to PhotoImage for Tkinter
icon = ImageTk.PhotoImage(icon_image)

#set window size
win1.geometry("400x600")

# Make the window resizable
win1.resizable(True, True)

# Create a frame to allow the image to expand
frame = tk.Frame(win1, bg="#121212")
frame.pack(expand=True, fill=tk.BOTH)

# Display the image in a label, using pack with expand options
logo_image = tk.Label(frame, image=icon, bg="#121212")
logo_image.pack(expand=True)

# Place image at the top center
logo_image.pack(side=tk.TOP, pady=10)

# Place image at the bottom
#logo_image.pack(side=tk.BOTTOM, pady=10)


#maintain aspect ratio when resized
win1.bind("<Configure>", maintain_aspect_ratio)

#icon = PhotoImage(file=f"icon_v1_nobg.png")

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