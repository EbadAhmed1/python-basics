'''

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")


for x in range(1, 11):
    print(x)



for x in reversed(range(1,11,2)):
    print(x)

credit_card = "1234-5678-9012"

for x in credit_card:
    print(x)


for x in range(1, 21):
    if x == 13:
        continue
    else
        print(x)

'''

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

