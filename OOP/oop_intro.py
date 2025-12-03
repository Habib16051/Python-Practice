# An object has a state and behaviors. To create an object, you define a class first. 
# And then, from the class, you can create one or more objects. 
# The objects are instances of a class.

class Person:

    # Def __init__(self, name, age):: This is the initializer method (constructor) for the Person class.
    # It is automatically called when an instance (object) of the class is created.

    def __init__(self, name, age):
        self.name = name  # instance of a person class
        self.age = age  # another instance of a person class

    def greet(self):
        return f"Hi, it's {self.name}"


result = Person('John', 28)  # Create a new Person object
result2 = Person('Ekjon Mayaboti', 25)  # Create a new Person object

print(result.name, result.age)
print(result2.name, result2.age)
print(result2.greet())


# Single inheritance
# A class can reuse another class by inheriting it. When a child class inherits from a parent class,
# the child class can access the attributes and methods of the parent class.

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return f"Hi, it's {self.name} and I'm a {self.job_title}"


employee_1 = Employee('Md Habibur Rahman', 28, 'Jr Software Engineer')
employee_2 = Employee('Ekjon Mayaboti', 25, 'HouseWife')
print(employee_1.greet())
print(employee_2.greet())
