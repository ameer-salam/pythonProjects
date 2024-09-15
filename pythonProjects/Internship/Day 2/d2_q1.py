#initialize array with 5 no and add new no to the array and print the updated array
arraY=[1,2,3,4,5]

#adding by append
arraY.append(1)
for i in arraY:
    print(i)
print("End!\n\n")

#adding by replacement
arraY[2] = 6
print("The updated array is : ")
for i in arraY:
    print(i)