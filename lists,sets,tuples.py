'''
List = []  Ordered and changeable. Duplicates OK
Set = {}   unordered and immutable, Add/Rem ok . NO Duplicates
TUPLE = () ordered and unchangeable. Duplicates OK.Faster

fruits = ["apple","orange","banana","coconut"]
# print(dir(fruits))
# print(len(fruits))
 
# print ("apple" in fruits)
# print(fruits[0:3])
# print(fruits[::2])

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits.index("apple")
# fruits.count("pineapple")

 for x in fruits:
    print(x)


fruits = {"apple", "orange", "banana", "coconut"}

print(fruits)
# print(fruit[0]) cant use
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

fruits = ("apple", "orange", "banana", "coconut")

# print(fruits.index("apple"))
# print(fruits.count("coconut"))


# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit)")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("--- YOUR CART ---")
for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total is ${total}")



# 2D Lists

fruits =     ["apples", "orange", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])

groceries = [["apples", "orange", "banana"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

'''

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*",0, "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()