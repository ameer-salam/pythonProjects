
#  Python program that takes user input to add multiple elements to an array and then prints the final array:
num = []

n_ele = int(input("enter the number of elements do you want to add to the array? "))

for i in range(n_ele):
    ele = int(input(f"Enter element {i+1}: "))
    num.append(ele)

# Print the final array
print("Final array:", num)