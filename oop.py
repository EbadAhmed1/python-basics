# object = A "bundle of related attributes and methods"

# class = (blueprint) used to design the structure and layout of an object

"""

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

car1.stop()
car2.stop()

print(car1.model)
print(car2.model)

"""

# class variables = Shared among all instances of a class

# all objects share same version unlike instance

class Student:
    
    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name 
        self.age  = age
        Student.num_students += 1

student1 = Student("Patrick",35)
student2 = Student("Jack",28)

print(student1.age)
print(student1.class_year)
print(Student.num_students)