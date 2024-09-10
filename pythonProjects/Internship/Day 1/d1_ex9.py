#Create a program that stops printing numbers when it encounters a number greater than 5 using the break statement. 
i=0
for i in range(0, 11):
    if(i>5):
        break
    else:
        print(i)