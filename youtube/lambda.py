'''x = lambda a : a + 10
print(x(5))'''

'''sum  = lambda pp : pp+10
print(sum(10))'''
x = lambda a, b : a * b
print(x(5, 6))


muti = lambda a, b : a * b
print(muti(5, 5))

three = lambda a, b, c: a + b * c
print(three(3, 4, 5))


def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print(sum)    
adder(2,3,4)
