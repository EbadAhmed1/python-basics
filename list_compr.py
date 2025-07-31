# List comprehension

"""

doubles = []

for x in range(1,11):
    doubles.append(x*2)

print(doubles)

doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]

print(triples)
print(doubles)

fruits = ["apple","orange","coconut"]

fruit_chars = [fruit.upper() for fruit in fruits]

print(fruit_chars)

numbers = [1,-2,-4,5,-6]
pos_nums = [num for num in numbers if num>=0]
neg_nums = [num for num in numbers if num<0]
even_numbs = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num%2 == 1]

print(pos_nums)

"""