lists = ["a","c", "a", "x", "r"]
lists = list(dict.fromkeys(lists))
print(lists)

names = ["amaka", "chinma", "john", "chinma", "amaka"]
names = list(dict.fromkeys(names))
print(names)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)