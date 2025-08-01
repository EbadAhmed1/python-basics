"""

# Inheritance = Allow a class to inherit attributes and methods from another class

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

dog = Dog("Scooby")
cat = Cat("Garfield")

print(dog.name)
print(dog.is_alive)
cat.eat()


#Multiple Inheritance = inherit from more than one parent class

#Multilevel Inheritance = inherit from a parent which inherits from another parent

class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
fish.hunt()

"""
# super() Function used in a child class to call methods from a parent class

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # method overriding
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()

class Square:
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

circle = Circle("red",True,5)

print(circle.color)