# # def ooo():
# #     a = int(input("input a number: "))
# #     b = int(input("input anothrr number: "))
# #     add = a+b
# #     print(add)

# # ooo()   
# #  #argument and parameter
# #  #the (a,b) is the parameter and the (1,3) is the argument
# # def sum (a,b):
# #      firstNo = a
# #      secondNo =b
# #      print(firstNo + secondNo)

# # sum(1,3) 

# # #returning a value
# # '''def sub (a,b):
# #     no1 =a
# #     no2 =b
# #     add =no1 + no2
# #     return add
# # ans = sub(20,20)
# # print(ans)  '''

# # def area (r):
# #     radius = r
# #     circleArea = (22/7*(radius**2))
# #     return circleArea
# # tita = area(20)    
# # #print(tita)

# # def another (tita, r):
# #     tita = tita
# #     radius = r
# #     circleArea = (tita/360)*(22/7*(radius**2))
# #     print("the sector of a circle ", circleArea)

# # another(tita, 20)

    

# # def my_function(fname):
# #   print(fname + " Refsnes")

# # my_function("Emil")
# # my_function("Tobias")
# # my_function("Linus")

# def my_function():
#     country = 'JOHN'
#     print(country)

# my_function()

# def name(fname):
#     print("my name is "+ fname)

# name("emeka")

# def names(firstname, lastname):
#     print(firstname,lastname)
# names("john", "boma")  

# def listss(lists = [1, 2, 3, 4]):
#     print(lists)
# listss()

def password(passwords = input("enter a password: ")):
    if len(passwords) < 8:
        print("password not good")
    else:
        print("done")    


password()

# def form(name = input("enter your name: "),
#           age = input("enter your age: "),
#           password = input("enter a password: ")):
#         #   if  name > 10:
#         #       print("check your name well.")
#           if password < 8: 
#               print("check your password")
#           else:
#               print(f"dear {name}, your form is submitted")     

# form(name,password,age)              


