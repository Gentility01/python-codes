"""3) A store charges $12 per item if you buy less than 10 items.
 If you buy between 10 and 99
items, the cost is $10 per item.
 If you buy 100 or more items, the cost is $7 per item.
  Write a program that asks the user how many items they are buying
   and prints the total cost."""

storeCharge = eval(input("how many items did you buy : ")) 

if storeCharge <= 10:
     print("your charges is $12")
if storeCharge >=11 and storeCharge <=99:
    print("your charges cost $10 ")
if storeCharge > 100:
    print("your charges costs $7 ")    