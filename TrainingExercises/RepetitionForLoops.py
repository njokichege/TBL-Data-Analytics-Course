#For_Loop_Basics
print("---For_Loop_Basics---")
basket_items = ['apple','banana','orange','grapes']
for fruit in basket_items:
    print(f"Item : {fruit}")
lst = [1,2,3,]
for i in range(len(lst)):
    print(lst[i],end = "\n")
for j in range(1,6):
    print(j,end = "\n")
store_items=[1,2,3,4,5]
itemCost = 2.50
totalCost = 0.0
for item in store_items:
    totalCost = itemCost + totalCost
print(totalCost)

#Nested Loops
print("---Nested Loops---")
items = ["apple","banana","orange"]
prices = [1.00,0.50,0.75]
for item in items:
    for price in prices:
        print(f"The price of {item} is ${price}")
for num in range(1,10):
    if num % 2 !=0:
        print("----------------")
        prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                prime = False
        if prime and num != 1:
            print("Prime Numbers Pure: ",num,end="\n")
storeItems = ["apple","grape","wheat"]
storeItemPrices = [25,400,3000]
unitsSold = 3
totalRevenue = 0
for item in storeItems:
    for price in storeItemPrices:
        totalRevenue = (unitsSold*price)+totalRevenue
print(totalRevenue)

#Looping with Range
print("---Looping with Range---")
for i in range(1,11,2):
    print(i)
for i in range(2,11,2):
    print(i)

#For Loop with Break Statement
print("---For Loop with Break Statement---")
store_items_2 = ["apple","banana","orange","grapes","watermellon"]
for item in store_items_2:
    print("Checking item : ",item)
    if item == "grapes":
        print("Found grapes! Exiting loop")
        break
numList = [1,2,3,4,5,6,7,8,9,10]
for num in numList:
    if num > 5:
        break
    else:
        print(num)

#For Loop with Continue Statement
print("---For Loop with Continue Statement---")
storeItems3 = ['apple','banana','orange','grape','watermelon']
for item in storeItems3:
    if item == 'orange':
        continue
    print(f"Item : {item}")
storeItems4 = ['apple','banana','orange','grape','watermelon']
for item in storeItems4:
    if item == 'banana':
        continue
    print(f"Item : {item}")


