#While Loop Basics
print("---While Loop Basics---")
m = 5
i = 0
while i < m:
    print(i,end=" ")
    i = i + 1
print("End")
numItems = 0
while numItems < 10:
    print(f"Adding item {numItems + 1} to the store")
    numItems += 1
print("All items have been added to the store")
itemCost = 5
amountSpent = 0
while amountSpent < 50:
    amountSpent = amountSpent + 5
    print(f"Add item to basket. Total = {amountSpent}")
print(f"Total bill = {amountSpent}")

#While Loop Break
print("---While Loop Break---")
count = 0
while count < 5:
    print("Count",count)
    if count == 2:
        break
    count += 1
challengeCount = 0
while challengeCount < 10:
    print(challengeCount)
    if challengeCount == 7:
        break
    challengeCount = challengeCount + 1

#While Loop Continue
print("---While Loop Continue---")
count2 = 0
while count2 < 5:
    count2 += 1
    if count2 == 3:
        continue
    print("Count is: ",count2)
num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0:
        print(num)
    else:
        continue

#While Loops with Lists
print("---While Loops with Lists---")
myList = [1,2,3,4,5]
index = 0
while index < len(myList):
    print(myList[index])
    index += 1
countList = [1,2,3,4,5,6,7,8,9,10]
countListIndex = 0
sumOfEven = 0
while countListIndex < len(countList):
    if countList[countListIndex] % 2 == 0:
        sumOfEven = sumOfEven + countList[countListIndex]
    countListIndex = countListIndex + 1
print(f"Sum of even : {sumOfEven}")
    