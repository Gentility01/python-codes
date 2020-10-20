def ooo():
    a = int(input("input a number"))
    b = int(input("input anothrr number "))
    add = a+b
    print(add)

ooo()   
 #argument and parameter
 #the (a,b) is the parameter and the (1,3) is the argument
def sum (a,b):
     firstNo = a
     secondNo =b
     print(firstNo + secondNo)

sum(1,3) 

#returning a value
'''def sub (a,b):
    no1 =a
    no2 =b
    add =no1 + no2
    return add
ans = sub(20,20)
print(ans)  '''

def area (r):
    radius = r
    circleArea = (22/7*(radius**2))
    return circleArea
tita = area(20)    
#print(tita)

def another (tita, r):
    tita = tita
    radius = r
    circleArea = (tita/360)*(22/7*(radius**2))
    print("the sector of a circle ", circleArea)

another(tita, 20)

    


