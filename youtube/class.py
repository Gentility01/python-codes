# class Point:
#     def move(self):
#         print("move")

#     def  draw(self):
#         print("draw")  

# #object(instance of a class)
# point1 = Point()
# #attributes(variable thaty belong to a particular object)
# point1.x = 10+10
# point1.y = 20
# print(point1.x, point1.y)
# #another example of an attribute
# point2 = Point
# point2.a =40
# point2.b =60
# print(point2.a)
# print(point2.b)



# point1.move()          

# #CONSTRUCTOR(is a function that get called at the point of creating an object)
# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def talk(self):
#         print("talk")

# name = Person("john bull")
# print(name.name)
# name.talk()

# class PersonSchool:
#     def __init__(self, school):
#         self.school = school

# school = PersonSchool("abiapoly")
# print(school.school)        

# class Religion:
#     def __init__(self, church):
#        self.church = church

# church = Religion("Anglican")
# print(church.church)     

# class Road:
#     def __init__(self, name):
#         self.name = name

# name = Road("school road")
# print(name.name)   

# class Person:
#     def talk(self):
#         print("i can talk")

# john =Person()
# john.talk()   

# class Construct:
#     def __init__(self, person):
#         self.person = person
        

# john = Construct("constructor") 
# print(john.person)  

# class  Persons:
#     def name(self):
#         first_name = input("enter your name: ")
#         if first_name == "douglas":
#             print("good")
#         else:
#             print("wrong name")    

#     def school(self):
#         name_of_school = input("enter the name of your school")
#         if name_of_school == "abiapoly":
#             print("correct")
#         else:
#             print("wrong school")           

# person  = Persons()
# person.name() 
# person.school()   

# class Person1:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"hi i am {self.name}")

# another = Person1("john smith")
# # print(another.name)
# another.talk()  

# second_person = Person1("amanda")
# second_person.talk()
# third_person = Person1("douglas")
# third_person.talk()

#INHERITANCE(mechsnism for re-using code)

class Mammals:
    def talk(self):
        print("can talk")


class Dog(Mammals):
    def bark(self):
        print("can bark")


class Cat(Mammals):
    pass

dog1 = Dog()
dog1.talk()
dog1.bark()        


cat1 = Cat()
cat1.talk()