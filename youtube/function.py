def My_function():
    start_game = input("enter a command >>> ")
    game = {
    "help" : """
    start -> to start.
    stop -> to stop.
    quit -> to quit.
    """,
    "start" : "your car is started",
    "stop" : "your car have stoped",
    }
    output = ""

    for fact in start_game:
        output += game.get(start_game, "!")
        break

    print(output)    

   #end of my function









def greet_user():
    print("hello word")
    print("how are you")


greet_user()    

#PARAMETERS AND ARGUMENT
# parameters pieace of information supplied to a function
#argument are values we supply to a function
def call_user(firstname, lastname):
    print(f"dear {firstname} {lastname}")

call_user("amaka", "douglas")
call_user("ebuka", "amanfu")

#KEYWORD ARGUMENTS
def names(first_name, last_name):
    print(f"dear {first_name}, {last_name}")

names(last_name = "nnamdi", first_name = "john")    


#RETURN STATEMENT
def square(numbers):
    return numbers*numbers

# result = square(3)
# print(result)
print(square(3)) 

My_function()