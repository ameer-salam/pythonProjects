import os
import sqlite3
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hashlib
import base64
import pyotp
import time

#corefunction to generate the OPT
# Decode the secret key (assuming it's base32 or base64 encoded)
def opt_gen(secret_key):
    try:
        decoded_key = base64.b32encode(secret_key.encode())
    except Exception as e:
        print("Failed to decode the secret key:", e)
        return None

    # Create a TOTP object using the decoded key
    totp = pyotp.TOTP(decoded_key)

    # Generate the current OTP
    current_otp = totp.now()

    return current_otp

# Path to the user database
user_db = "user.db"
user_db_keys="user_keys.db"

#insert the keys into the keys db
def insert_into_keys_db(key, provider):
    conn=sqlite3.connect(user_db_keys)
    cursor=conn.cursor()
    try: 
        cursor.execute('''INSERT INTO user_keys(secret_key, provider) VALUES(?, ?)''', (key, provider))
        conn.commit()
        print("Key Added Successfully")
    except sqlite3.IntegrityError:
        print("Failed to insert the Key!")
    finally:
        conn.close()

    return True


#def to add new keys
def add_new_key(key):
    os.system("cls")
    print("Remember to copy and paste the secret keys clearly : ")
    provider=input("Enter the Provider/Service : ")
    secret_key=input("Enter the Secret Keys : ")
    encrypted_secret_key=encrypt_content(secret_key, key)
    encrypted_provider=encrypt_content(provider, key)
    key_insertion_status = insert_into_keys_db(encrypted_secret_key, encrypted_provider)
    if key_insertion_status==True:
        os.system('cls')
        print("Displaying the Existing Keys: ")
        display_keys(key)

#function to display the existing keys
def display_keys(key):
    conn=sqlite3.connect(user_db_keys)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM user_keys")
    count=cursor.fetchone()[0]
    if count==0:
        print("No keys Exist!")
        print("Enter your first key")
        add_new_key(key)
    else:
        os.system("cls")  # Clear the console
        print(f"The Keys existing are:")

        cursor.execute('''SELECT * FROM user_keys''')
        rows = cursor.fetchall()

        if rows:
            optio = ""
            while not (optio == 'exit'):
                os.system('cls')  # Clear the screen at the beginning of each loop
                print("Keys in the database:")
                
                # Loop through and display each key with OTP
                for row in rows:
                    secret_key = decrypt_content(row[1], key)
                    provider = decrypt_content(row[2], key)
                    otp = opt_gen(secret_key)
                    print(f"ID: {row[0]}, OTP: {otp}\t\t Provider: {provider}")
                
                time.sleep(30)
                optio = input("To Enter New Keys type Y/y: \nType 'exit' to EXIT or press Enter to refresh:")
                
                if optio == 'exit':
                    break
                elif optio.lower() == 'y':
                    add_new_key(key)
        else:
            print("No keys found in the database.")
    
    conn.close()
    display_keys(key)

#function to check if the key database if not existing. if existing then connect
def check_key_db():
    conn = sqlite3.connect(user_db_keys)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_keys(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    secret_key TEXT NOT NULL,
                    provider TEXT NOT NULL)''')
    
    conn.commit()  # Ensure the creation is committed to the database
    print("Key database checked or created if not existing")
    
    return conn  # Return the open connection for further operations



# Function to check if user DB exists
def get_user():
    return os.path.exists(user_db)

# Function to derive a 256-bit AES encryption key from a password
def derive_key(password):
    return hashlib.sha256(password.encode()).digest()

# Function to encrypt content using AESGCM
def encrypt_content(content, password):
    key = derive_key(password)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 12-byte nonce
    encrypted_data = aesgcm.encrypt(nonce, content.encode(), None)
    # Use base64 encoding to return the nonce + encrypted data as an ASCII string
    return base64.b64encode(nonce + encrypted_data).decode('utf-8')

def decrypt_content(encrypted_content, password):
    key = derive_key(password)
    aesgcm = AESGCM(key)
    encrypted_data = base64.b64decode(encrypted_content)
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    try:
        return aesgcm.decrypt(nonce, ciphertext, None).decode('utf-8')
    except:
        return None  # If decryption fails, return None
    

# Create a new user in the database
def create_new_user():
    conn = sqlite3.connect(user_db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      encrypted_username TEXT NOT NULL)''')
    conn.commit()
    
    password_verified = False
    while not password_verified:
        user_name = input("User name          : ")
        password1 = input("Enter password     : ")
        password2 = input("Re-enter password  : ")
        
        if password1 == password2:
            password_verified = True
        else:
            print("Passwords did not match! Please re-enter.")
    
    # Encrypt the username with the password
    encrypted_username = encrypt_content(user_name, password2)
    
    try:
        cursor.execute("INSERT INTO user (encrypted_username) VALUES (?)", (encrypted_username,))
        conn.commit()
        print("User account created successfully.\nRe-run the program to get started")
    except sqlite3.IntegrityError:
        print("Error occurred while creating the account.")
    finally:
        conn.close()

# Function to print usernames in the database (encrypted)
def print_usernames():
    conn = sqlite3.connect(user_db)
    cursor = conn.cursor()
    cursor.execute("SELECT id, encrypted_username FROM user")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"Stored Username(Encrypted): {row[1]}")
        return rows[0][1]  # Return the first encrypted username
    
    conn.close()


# Main function
def main():
    print("\n\nWelcome to OpenAuth\n")
    user_exists = get_user()
    if not user_exists:
        print("No user account found. Create a new account.")
        create_new_user()
    else:
        print("User account found!\n")
        encrypted_user = print_usernames()  # Get the encrypted username
        if encrypted_user:  # Check if there is an encrypted user
            key = input("Enter the Master Key to decript the Database: ")
            decrypted_username = decrypt_content(encrypted_user, key)
            if decrypt_content:
                print(f"Logged into : {decrypted_username}")
                conn=check_key_db()
                display_keys(key)

                conn.close()
            else:
                print("Failed to decrypt the username. Incorrect key or corrupted data.")
        else:
            print("No encrypted user data found.")
        

if __name__ == "__main__":
    main()