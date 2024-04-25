#Function Basics
print("---Function Basics---")
def greet():
    print("Hi!")
greet()
def display_store_hours():
    print("Operating hours = 168")
display_store_hours()

#Function Parameters
print("---Function Parameters---")
def calculate_total_price(item_price, quantity):
    total_price = item_price*quantity
    return total_price
item_price = 10
quantity = 5
total = calculate_total_price(item_price,quantity)
print("Total price : ",total)
def calculate_discounted_price(original_price,discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage/100)
    return discounted_price
original_price = 150 
discount_percentage = 10
print(calculate_discounted_price(original_price,discount_percentage))

#Return Statements
print("---Return Statements---")
def calculate_square(num):
    square = num * num
    return square
result = calculate_square(5)
print(result)
def calculate_discount(original_price,discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price
