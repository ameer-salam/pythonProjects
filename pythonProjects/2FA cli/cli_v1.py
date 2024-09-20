#library files
import tkinter as tk

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

#create main window
win1 = tk.Tk()

#set window title
win1.title("2FA by Ameer Salam")

#set window size
win1.geometry("400x600")
#maintain aspect ratio when resized
win1.bind("<Configure>", maintain_aspect_ratio)

#set background colour
win1.config(bg="white")

#start the tinkter loop
win1.mainloop()