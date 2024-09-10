#Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero. 
no=int(input())
if(no==0):
    print("zero!")
elif(no<0):
    print("Negative")
else:
    print("Positive")