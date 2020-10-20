'''name = input('enter your name: ')
yearOfBirth = int(input('enter your birth year : '))
age = 2020 - yearOfBirth
print(type(yearOfBirth))
print(type(name))
print('dear ' +name + ' your age is ' + str(age))'''

fullName = input("enter your full name : ")
yearOfBirth = input("enter your birth year : ")
age = 2020 -int(yearOfBirth)
#print("dear " + fullName + " your age is " + str(age)) 

pounds = float(input("enter your weight in lbs : "))
km = pounds * 0.45
print("dear " + fullName.upper() + " you weigh " + str(km) + "km " +  " and your age is " + str(age))
print(f'dear {fullName.upper()} you weigh {str(km)}km and your age is{str(age)}')
