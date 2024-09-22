import sqlite3
import os

user_db = "users.db"

#add new user
def new_user():
    user_name=input("Enter user name: ")
    pass1=input("Enter the password : ")
    pass2=input("Renter the password : ")
    if(pass1==pass2):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            # Insert new user into the database
            cursor.execute('INSERT INTO user (username, password) VALUES (?, ?)', (user_name, pass2))
            conn.commit()
            print(f"User '{user_name}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Username '{user_name}' already exists.")
        finally:
            conn.close()

        print("user created")

    
    


# Function to connect to the database (create if not exists)
def connect_to_db():
    conn = sqlite3.connect(user_db)
    return conn

#count the number of users
def count_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM user")  # Count rows in the 'user' table
    user_count = cursor.fetchone()[0]  # Fetch the count
    conn.close()
    return user_count

# Function to create the 'user' table if it doesn't exist
def create_db():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL)''')
    conn.commit()
    conn.close()
    print("Table has been created")
    connect_to_db()

def check_db():
    if not os.path.exists(user_db):
        print("Database not found! Creating one...")
        create_db()
    else:
        print("Database found, proceeding...")
        connect_to_db()  # Ensure the table exists even if the DB file is found

# Main function to check and create the database if needed
def main():
    os.system('cls')
    conn=check_db()
    count = count_users()
    print(f"The number of users are: {count}")
    if count==0:
        print("No user found!\n")
        new_user()
    else:
        print("Slect the below options: ")
        print("LogIn to current users")

if __name__ == "__main__":
    main()