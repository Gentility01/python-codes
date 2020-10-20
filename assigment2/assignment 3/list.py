#(1) append
#adds  another element to the list
fruits = ["apples", "mango"]
fruits.append("orange")
print(fruits)

'''names = ["amaka", "ada"]
names.append("nnamdi")
print(names)'''

#(2) counts
#counts the number of element entered in a list 
names = ["amaka", "nnamdi", "john"]
pname = names.count("john")
print(pname)

#(3) extend
#extends or add two lists together to be one list
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

#(4) sort
cars =['amanda', 'ford', 'benz']
motor = cars.sort()
print(motor)

#(5) pop
#removes the first element in the car list
cars = ['motor', 'benz', 'ford']
cars.pop(1)
print(cars)

#(6) reverse
#reverse the order of the list
classes  =["js1", "js2", "js3"]
classes.reverse()
print(classes)

#(7) index
#provides the position of a certin element
colors = ['blue', 'black', 'yellow']
color =colors.index('black')
print(color)

#(8) copy
courses = ['english', 'maths', 'chemistry']
myCourses = courses.copy()
print(myCourses)

#(9) clear
#removes all element from the list
prices = [10000, 20000, 30000]
prices.clear()
print(prices)

#(10) insert
#inserts an element to a list by assigning the value to it first
prices = [10000, 20000, 30000]
prices.insert( 2,40000)
print(prices)
