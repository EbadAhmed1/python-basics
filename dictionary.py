"""

capitals = {"USA" : "Washington D.C",
            "India": "New Delhi",
            "Russia": "Moscow"}


#print (dir(capitals))
#print(capitals.get("Russia"))

if capitals.get("Russia"):
    print("Capital exists")
else:
    print("Capital doesnt exist")

capitals.update({"Germany": "Berlin"})
capitals.popitem()
capitals.clear()


keys = capitals.keys()

values = capitals.values()
print(capitals)

print(values)

# keys and values both in items method


for key, value in capitals.items():
    print(f"{key}: {value}")


# Concession stand program 

menu = {"pizza": 3.00,
        "chips": 1.00,
        "soda": 3.00}
cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+= menu.get(food)
    print(food, end=" ")

print()
print(f"The total is ${total:.2f}")


import random

# print (help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
# random.shuffle()

# print(number)



import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
# elif three times

"""
