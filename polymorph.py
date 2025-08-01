"""

# Polymorphism = Many Forms

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# square = Square()

shapes = [Circle(4), Square(5)]

for shape in shapes:
    print(f"{shape.area()}cm^2")

"""
# Duck Typing = Another way to achieve polymorphism
#               Object must have the min necessary attributes/methods

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    print(animal.alive)
