
""""
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("Outdoor event is not cancelled")

"""
temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")

elif temp <=0 and is_sunny:
    print("It is COLD outside")

elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside ")

elif temp >= 28 and not is_sunny:
    print("It is HOT outside")

