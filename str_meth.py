
"""""
name = input("Enter your full name: ")
phone_no = input("Enter your phone number: ")

#result = name.find("o")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
result = name.isalpha()
res = phone_no.count("-")
phone_no = phone_no.replace("-"," ")

print(result)
print(res)
print(phone_no)

username = input("Enter a username ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}")

"""

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

last_digits = credit_number[-4:]

# reverse a string
# credit_number = credit_number[::-1]

print(f"XXXX-XXXX-XXXX-{last_digits}")