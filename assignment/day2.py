"""
1)Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

2)Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over

3) A store charges $12 per item if you buy less than 10 items.
 If you buy between 10 and 99
items, the cost is $10 per item.
 If you buy 100 or more items, the cost is $7 per item.
  Write a program that asks the user how many items they are buying
   and prints the total cost.

4)A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.

"""


"""
1)Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

"""

 
a = int(input("enter a length: "))
if a < 0:
    print("negative value")
else:
    print(a*2.54)



"""
2)Write a program that asks the user how many credits they have taken.
 If they have taken 23
or less, print that the student is a freshman.
 If they have taken between 24 and 53, print that
they are a sophomore. 
The range for juniors is 54 to 83, and for seniors it is 84 and over
"""
a = int(input("enter a value"))
if a <= 23:
    print("fresh man")


"""
4)A year is a leap year if it is divisible by 4, 
except that years divisible by 100 are not leap years
unless they are also divisible by 400. 
Write a program that asks the user for a year and prints
out whether it is a leap year or not.
"""
    

"""year = int(input("enter a year"))
if ((year % 4 == 0) and (year % 100 != 0)) or(year % 400 == 0):
    print("this is a leap year")
else:
    print("this is not a leap year")    """


