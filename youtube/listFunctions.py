#to add anumber to a listt
numbers =  [5,3,5,67,89]
numbers.append(13)
print(numbers)

#place an item in a specific index
numbers = [1,2,3,4,5,6,7,8]
numbers.insert(1,20)
print(numbers)
#to remove an item
numbers = [2,4,6,8,9]
numbers.remove(9)
print(numbers)
#remove all the items
numbers =[0,0,0,0,0,]
numbers.clear()
print(numbers)

#remove the last item
numbers = [2,3,5,7,8]
numbers.pop()
print(numbers)

#to check an index in a value
numbers = [2,3,5,7,8]
print(numbers.index(5))
#checking for the existance of a number in a list(boolean)
numbers = [1,2,3,4,5]
print(5 in numbers)

#to count numbers of lists
numbers = [1,2,4,6,3,6]
print(numbers.count(6))

#to sort a list
numbers = [2,3,4,5,6,7]
numbers.sort()
print(numbers)
# to reverse a list
numbers = [2,3,4,5,6,7]
numbers.reverse()
print(numbers)

#to copy a number
numbers = [3,4,5,6]
numbers2 = numbers.copy()
print(numbers2)

#to remove a duplicate of a number
numbers = [2,2,4,4,6,8,6,9,10]
removeNumber = numbers.count(2)
print(removeNumber.remove())

