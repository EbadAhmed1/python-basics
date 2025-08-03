
#Exception Handling

try:
    number = input("Enter a number")
    print(1 / number)
except ZeroDivisionError
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
# except Exception:      catches all exceptions
# finally:   always ex
#    print("Do some cleanup")

"""
#Decorator ; Extends the behaviour of another function

def add_sprinkles(func):
    def wrapper(*args,**kwrags):
        print("You add sprinkles")
        func(*args,**kwrags)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwrags):
        print("You add fudge")
        func(*args,**kwrags)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream")

get_ice_cream("chocolate")
"""