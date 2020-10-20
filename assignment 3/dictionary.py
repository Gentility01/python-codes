'''person = {
    "name" : "Uba",
    "courses" : "computer science",
    "age" : 24

}
print(person)'''
#(1) clear removes all the element in the list
person = {
    "name" : "Uba",
    "courses" : "computer science",
    "age" : 24

}
person.clear()
print(person)

#(2) copy
#copy all the element
person = {
    "name" : "amadi",
    "age"  : 30,
    "occupation" : "student"
}
person.copy
print(person)

#(3) from key
#retuns a dictionary with a specified key and value
x = ("key1", "key2", "key3")
y = (0)
lis = dict.fromkeys(x,y)
print(lis)

#(4) get
#returns the value of specified key
'''import  requests

x = requests.get('https://google.com')
print(x.status_code)'''

#(5) item
#retuns the dictionartry's key value pairs
person = {
    "name" : "amanda",
    "school": "abia poly",
    "year" : 2020
}
x = person.items()
print(x)

#(6) keys
#returns the keys
person = {
    "name" : "amanda",
    "school": "abia poly",
    "year" : 2020
}
x = person.keys()
print(x)

#(7) pop
#removes an element from a list

fruits = ["mango", "orange", "banana"]
fruits.pop(1)
print(fruits)

#(8) popitem
# removes the last item in a list
person = {
    "name" : "amanda",
    "school": "abia poly",
    "year" : 2020
}
person.popitem()
print(person)

#(9) setdefault
'''
The setdefault() method returns the value
of the item with the specified key.
If the key does not exist, insert the key,
with the specified value, 
'''
person = {
    "name" : "uba",
    "school" : "rcc",
    "hobby" : "football"
}

x =person.setdefault("school","abiapoly")
print(x)

age = {
   "amadi" : 30,
   "john": 34,
}
x = age.setdefault("nnamdi", 50)
print(x)

#(10) update
#insert an item to the dictionary
age = {
   "amadi" : 30,
   "john": 34,
}
age.update({"nnamdi" : 50})
print(age)

#value
#returns the list of allthe vslue in a dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

