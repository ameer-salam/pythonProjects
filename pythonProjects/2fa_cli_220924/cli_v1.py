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

#function to log into database
def login(username, e_username, key):
    conn = sqlite3.connect(user_db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_key(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   secret_key TEXT NOT NULL,
                   provider TEXT NOT NULL)''')
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM user_key")
    count=cursor.fetchone()[0]
    if count==0:
        print("No keys Exist!")
        #adding new key
        os.system('cls')
        sec_key=input("Enter Secret key : ")
        sec_key_provider=input("Enter provider : ")
        sec_key_encrypted=encrypt_content(sec_key, key)
        sec_key_provider_encrypted=encrypt_content(sec_key_provider, key)
        try:
            cursor.execute("INSERT INTO user_key(secret_key, provider) VALUES(?,?)", (sec_key_encrypted, sec_key_provider_encrypted))
            conn.commit()
            print("Key added Successfully")
        except sqlite3.IntegrityError:
            print("Error occured during key insertion")
        finally:
            conn.close()
    conn.close()
    return count

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
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                    encrypted_username TEXT PRIMARY KEY,
                    twofa_secret TEXT,
                    provider TEXT)''')
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
    
    # You need to provide values for twofa_secret and provider (or pass None if not available)
    twofa_secret = ""  # For now, we're leaving it empty
    provider = ""      # For now, we're leaving it empty
    
    try:
        cursor.execute("INSERT INTO user (encrypted_username, twofa_secret, provider) VALUES (?, ?, ?)", 
                       (encrypted_username, twofa_secret, provider))
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
    cursor.execute("SELECT encrypted_username FROM user")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"Stored Username(Encrypted): {row[0]}")  # row[0] for the only selected column
        return rows[0][0]  # Return the first encrypted username
    
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
                os.system('cls')
                print(f"Logged into: {decrypted_username}")
                user_secret_key_db = f"{decrypted_username}_keys.db"
                key_count=login(decrypted_username, key, user_secret_key_db)
                key_disp(key_count)
            else:
                print("Failed to decrypt the username. Incorrect key or corrupted data.")
        else:
            print("No encrypted user data found.")
        

if __name__ == "__main__":
    main()
