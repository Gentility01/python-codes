'''
NESTED LOOP
nested loop adds one loop inside another loop
'''
for x in range(5):
    for y in range(5):
        print(f"(x{x}, y{y})")

numbers = [5, 2, 5, 2, 2, 5]
for x in numbers:
    print("x" * x)

number = [1, 1, 1, 1, 5 ]
for y in number:
    print("x" * y)    