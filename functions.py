"""

def happy_birthday(name, age):
    print(f"HBD {name}")
    print(f"you are {age} years old ")

happy_birthday("Bro",20)
happy_birthday("steve",30)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Joe",2000,"01/15")


def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

print(add(1,2))
print(subtract(1,2))


# DEFAULT ARG

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1))


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)


# keyword arguments

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello",title="Mr.",last="John",first="James")

print("1","2","3", sep=" ")



# arbitrary arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2,3))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("Dr.","Ebad","Ahmed")

# *args , **kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI")

def shipping(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end= " ")

shipping("Dr.", "Spongebob", "Sp", "III",
         streets="123 Fake St.",
         apt="100",
         city="Detroit")


# iterables

numbers = [1,2,3,4,5]

for number in reversed(numbers):
    print(number, end="-")


name = "Ebad Ahmed"

for char in name:
    print(char, end=" ")

my_dict = {"A":1, "B":2, "C":3}

for key, value in my_dict.items():
    print(key, value)


#membership op

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

"""

grades = {"Sandy": "A", "Squid": "B", "Patrick" : "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")