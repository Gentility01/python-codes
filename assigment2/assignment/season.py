"""
Write a Python program that reads two integers representing a month and day and 
prints the season for that month and day.

"""

days = int(input("enter a number of a day : "))
year = int(input("enter the number of the month : "))

if days ==7 :    
    print("today is saturday")
if days ==6 :
    print("today is friday")
if days ==5 :
    print("today is thusday")
if days ==4 :
    print("today is wednesday")
if days ==3 :
    print("today is tuesday")
if days ==2 :
    print("today is monday")
if days ==1 :
    print("today is sunday")

if year >=7 and year <=12:
        print("we are in dry season")
elif year >=1 and year <=6 :
        print("we are in raining season")   