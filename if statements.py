age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

respone = input("Would you like food? (Y/N): ")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")