"""

# import math
# import math as m
# from math import e
import example

# print(m.pi)
result = example.square(3)

print(result)

# scope resolution = LEGB Local -> Enclosed -> Global -> Built-In

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()


def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()


from math import e 

def func1():
    print(e)

e = 3

func1()


# if __name__ == __main__: (this script can be imported OR run standalone)

def main():
    print("This is script")

if __name__ == '__main__':
    main()

"""
import random

def spin_row():
    symbols = ['s1', 's2', 's3', 's4', 's5']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 's1':
            return bet * 3
        elif row[0] == 's2':
            return bet * 4
        elif row[0] == 's3':
            return bet * 10
        else:
            return bet * 5
    return 0  # Explicitly return 0 for no win

def main():
    balance = 100

    print("Welcome to Slots")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        if balance <= 0:
            print("Game Over! Your balance is depleted.")
            break

if __name__ == '__main__':
    main()
    