#hex converts a number to hexadecimals
x = hex(100)
print(x)
#id returns the unique id of tuple object
'''
The id is the object's memory address, and will be different for each time you run the program. 
(except for some object that has a constant unique id,
 like integers from -5 to 256)
'''

fruits = ("apples", "banana", "orange")
y = id(fruits)
print(y)

#oct retuns number to octal
x = oct(22)
print(x)