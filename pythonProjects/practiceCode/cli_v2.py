import os
import sqlite3
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hashlib
import base64

# Path to the user database
user_db = "user.db"

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
                print(f"Decrypted Username: {decrypted_username}")
            else:
                print("Failed to decrypt the username. Incorrect key or corrupted data.")
        else:
            print("No encrypted user data found.")
        

if __name__ == "__main__":
    main()
