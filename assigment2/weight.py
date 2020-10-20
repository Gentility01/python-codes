"""
3)A good program will make sure that the data its users enter is valid. Write a program that
  asks the user for a weight and converts it from kilograms to pounds. Whenever the user
 enters a weight below 0, the program should tell them that their entry is invalid and then ask
 them again to enter a weight. [Hint: Use a while loop, not an if statement].
"""
weight = float(input("enter your weight in km : "))
while weight>0:
    pounds = weight*4.5
    print(pounds)
    break
  
  
    
