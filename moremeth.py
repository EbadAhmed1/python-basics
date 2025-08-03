"""

# Static methods ; method that belongs to a class 
# Instance methods ; best for operation on instances of the class

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Cook"))


# Class Method ; Allow operations related to the class itself
#                (cls) as the first parameter, which represents the class itself.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

"""

# Magic Methods (Dunder methods)
# Allow dev to define or customize the behaviour of objects
#Automatically called by many of Python's built in op

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    #equal to
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    #less than
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    #similarly other methods greather than , add two objects

book1 = Book("Hobbit","JRR",310)
book2 = Book("Hobbit","JRR",190)

print(book1 < book2)
print(book1 == book2)
