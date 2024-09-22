#library files
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3

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

# Create or connect to the database
conn = sqlite3.connect("2fa_keys.db")
cursor = conn.cursor()

# Create table to store keys
cursor.execute('''
CREATE TABLE IF NOT EXISTS keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL
)
''')
#core function
def add_key_to_db(key: str):
    cursor.execute("INSERT INTO keys (key) VALUES (?)", (key,))
    conn.commit()
    print("Key stored in database.")



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
    icon_add_key = PhotoImage(file=f"add_key_v1_nobg.png")
    #set background colour
    win_add_key.iconphoto(False, icon_add_key)
    key_label=tk.Label(win_add_key, text="Enter or paste your Secret keys : ", bg="#272729", fg="white")
    key_label.pack(pady=20)
    key_entry = tk.Entry(win_add_key, width=40)
    key_entry.pack(pady=10)

    def key_input():
        secret_key=key_entry.get()
        print(f"The entered key is : {secret_key}")
        add_key_to_db(secret_key)
        key_entry.delete(0, tk.END)
    
    submit_button=tk.Button(win_add_key, text="Submit", command=key_input)
    submit_button.pack(pady=20)
    
    #set background colour
    win_add_key.config(bg="#272729")
    a = int(input("1/0"))
    if a==1:
        win_add_key.destroy()
        win1.geometry("400x600")
        win1.bind("<Configure>", maintain_aspect_ratio)
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



conn = sqlite3.connect("2fa_keys.db")
cursor = conn.cursor()

# Query to fetch all keys from the database
cursor.execute("SELECT * FROM keys")

# Fetch all the rows from the 'keys' table
all_keys = cursor.fetchall()

# Check if there are any keys stored
if all_keys:
    print("Stored 2FA keys:")
    countk=0
    for row in all_keys:
        row_count = cursor.fetchone()[0]
    print(f"Available keys are : {countk}")
else:
    print("No keys found.")

# Close the connection
#conn.close()




#start the tinkter loop
win1.mainloop()