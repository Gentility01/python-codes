'''
COMPARISM OPERATOR
> greater than
< lessthan
>= greater or equals
<= lessthan or equals
!= not equals
'''

temprature = 30

if temprature >= 30:
    print("hot temprature")
elif temprature  <=10:
    print("cold temprature")
else:
    print("its either cold or hot") 

name = input("enter a name here : ")

if len(name) <3:
    print("you need to enter a name more than 3 character")
elif len(name)>20:
    print("mazimum character to enter is enough")
else:
    print("good!")        

weight = int(input("enter your weight : "))

typ = input("in kg, or lb? : ")

kg = weight * 0.45
pounds = weight / 0.45

if typ == "kg":
    print(f"Dear {name} , your weight in kg is {kg} kilos")
if typ == "lb":
    print(f"Dear {name}, your weight in pounds is {pounds} pounds")    


    