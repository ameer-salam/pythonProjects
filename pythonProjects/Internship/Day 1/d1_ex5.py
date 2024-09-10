#Create a program that checks if a given year is a leap year. 
year=int(input("Enter the year : "))
if(year%4==0 and (year%100 != 0 or year%400 ==0)):
    print("the year ", year, " is a leap year!\n")
else:
    print("it is not a leap year")