'''
With the while loop we can execute a set of 
as long as a condition is true.
'''

# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i+ 1

#GUESS GAME
# secreat_number = 9
# guess_limit = 3
# guess_count = 0

# while guess_count < guess_limit:
#     guess = int(input("GUESS: "))
#     guess_count += 1
#     if guess == secreat_number:
#         print("YOU'VE WON!!!")
#         break
# else:
#     print("sorry you failed")        

# CAR GAME
command =""
while  True:
    command = input(">>> ").lower()
    if command == "start":
        print("Car is started...")
    elif command == "stop":
        print("Car stopped.") 
    elif command == "help":
       
        print("""
>>> start - to start the car.
>>> stop - to stop the car.
>>> quit - to quit
         """) 
    elif command == "quit":      
         break
    else:
        print("Sorry i don't understand") 

# while True:
#     name = input("enter your name: ")
#     grade = int(input("enter your grade: "))
#     if grade <= 20:
#         print(f"dear {name} your grade is F9.")
#     elif grade >=20 and  grade <=40:
#         print(f"dear {name} your grade is C6.") 
#     elif grade >=40 and grade <= 60:
#         print(f"dear {name} your grade is C4.")  
#     elif grade >=60 and grade <=80:
#         print(f"dear {name} your grade is B2.")
#     elif grade >= 80 and  grade  <=100:
#         print(f"dear {name} your grade is A1.")
#     else:
#         print("you loose")
# name = input("enter your name : ").upper()
# main_password = "gentility"    
# number_of_password_to_try = 3
# limit_of_password = 0

# while limit_of_password < number_of_password_to_try:
#     password = input("enter your password: ")
#     limit_of_password += 1
#     if password == main_password:
#         print(f"dear {name}, your password is correct")
#         break
#     elif password != main_password:
#         print("wrong try again")    
# else:
#     print(f"dear {name}, you cant enter another password... please check and try again")    

# password = input("enter your password: ")
# another_password = input("confirm your password: ")

# if password == another_password:
#     print("confirm")
# else:
#     print("wrong password")

# i = 1
# while i <= 5:
#     print("good " * i)

#     i = i + 1

