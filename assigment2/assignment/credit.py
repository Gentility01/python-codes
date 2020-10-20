"""2)Write a program that asks the user how many credits they have taken.
If they have taken 23
or less, print that the student is a freshman.
 If they have taken between 24 and 53, print that
they are a sophomore.
 The range for juniors is 54 to 83, and for seniors it is 84 and over"""

userInput = int(input('enter how many credit you have : '))
if userInput <= 23:
    print("you are a freshner")
if userInput >= 24 and userInput<=53:
    print("youre a sophmore") 
if userInput >= 54 and userInput<=83:
    print("you are ajunior")  
if userInput >=84 and userInput ==100:
    print("you are a senior")        