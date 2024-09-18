import pyotp
import time

key = pyotp.random_base32() #this generates the OTP

print(f"The key is {key}\n")