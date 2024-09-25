import pyotp
import time

key = pyotp.random_base32() #this generates the OTP
print(f"The key is {key}\n")

totp = pyotp.TOTP(key)
#print(f"The TOTP key is {totp}\n")

i=0
while (i<10):
    print(f"totp now is : {totp.now()}\n") #changes every 30 seconds
    time.sleep(30)