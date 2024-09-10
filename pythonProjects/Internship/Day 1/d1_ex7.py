#Create a program that prints the multiplication table of a given number using a while loop.
no=int(input("Enter the number : ")) #to print the prompt to take the input of the number
i=1 #to store the number 1 to 10
while i<11: #while loop
    print(f"{no} x {i} : {no*i}\n") 
    i+=1
