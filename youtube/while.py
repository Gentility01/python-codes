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

#CAR GAME
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

while True:
    name = input("enter your name: ")
    grade = int(input("enter your grade: "))
    if grade <= 20:
        print(f"dear {name} your grade is F9.")
    elif grade >=20 and  grade <=40:
        print(f"dear {name} your grade is C6.") 
    elif grade >=40 and grade <= 60:
        print(f"dear {name} your grade is C4.")  
    elif grade >=60 and grade <=80:
        print(f"dear {name} your grade is B2.")
    elif grade >= 80 and  grade  <=100:
        print(f"dear {name} your grade is A1.")
    else:
        print("you loose")
    
                
    break



