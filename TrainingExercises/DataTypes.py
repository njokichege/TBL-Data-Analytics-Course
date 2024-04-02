#Lists
print("---Lists---")
colours = ["red","blue","green","yellow"]
print(colours)
colours.append("purple")
print(colours)
colours.remove("green")
print(colours)

#Dictionaries
print("---Dictionaries---")
person = {
    "name":"John Doe",
    "age":30,
    "address":"123 Main Street"
}
print(person.values())
person["age"] = 31
person["phone"] = "555-555-55555"
del person["address"]
print(person.values())
product = {
    "name":"pencil",
    "price":10,
    "quantity":5
}
print(product.values())
product["price"] = 25
product["category"] = "school supplies"
del product["quantity"]
print(product.values())

#Tuples
print("---Tuples---")
store_items = ("apple","banana","orange","grape")
print(store_items[0])
print(store_items[1])
for item in store_items:
    print(item)
if "apple"in store_items:
    print("Apple is in the store items")
else:
    print("Apple is not in the store items")
coordinates = (3,4,5,6)
print(coordinates)
for item in coordinates:
    print(item)
if 3 in coordinates:
    print("3 exists")
else:
    print("3 doesn't exist")

