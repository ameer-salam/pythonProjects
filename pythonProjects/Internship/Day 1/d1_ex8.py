# Write a Python program that iterates through numbers 1 to 10 and prints each number. Use the continue statement to skip numbers that are divisible by 3.
i=0
for i in range(1, 11):
    if(i%3==0):
        continue
    else:
        print(f"{i}\n")
