email = input("enter an email adress : ")
if "@" in email and "." in email:
    print("sucess")
else:
    print("wrong email adress")    

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

x = lambda a : a + 10
print(x(5))