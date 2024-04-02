#If_Statement
print("---If_Statement---")
number = 15
if number > 10:
    print("The number is greater than 10")
n = 6
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
total_purchase = 100
if total_purchase > 50:
    print("Customer is eligible for a discount")
else:
    print("Customer is not eligible for a discount")

#If_Else_Statements
print("---If_Else_Statements---")
item_price = 50
wallet_balance = 30
if wallet_balance >= item_price:
    print("You can buy the item!")
else:
    print("You don't have enough money to buy the item.")
total_purchase_amount = 150
if total_purchase_amount > 100:
    print("You are eligible for 10% discount")
else:
    print("You are not eligible for 10% discount")

#Nested_If_Statements
print("---Nested_If_Statements---")
store_open = False
time = 10
if store_open:
    if time < 9:
        print("The store is open for breakfast")
    else:
        print("The store is open for lunch")
else:
    print("The store is closed")
tpa = 150
if tpa >= 100:
    if tpa >= 200:
        print("You are eligible for a 20% discount")
    else:
        print("You are eligible for a 10% discount")
elif tpa <= 100:
    print("You are not eligible for any discount")

#Chained_If_Statements
print("---Chained_If_Statements---")
x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x > 0:
    print("x is positive")
stpa = 350
if stpa == 100:
    print("10%")
elif stpa > 100:
    print("15%")
elif stpa >= 200:
    print("20%")
