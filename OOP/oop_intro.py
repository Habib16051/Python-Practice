# An object has a state and behaviors. To create an object, you define a class first. 
# And then, from the class, you can create one or more objects. 
# The objects are instances of a class.

class Person:

#def __init__(self, name, age):: This is the initializer method (constructor) for the Person class. 
# It is automatically called when an instance (object) of the class is created.

    def __init__(self, name, age):
        self.name = name #instance of a person class
        self.age = age #another instance of a person class

    def greet(self):
        return f"Hi, it's {self.name}"

result = Person('John',28) # Create a new Person object
result2 = Person('Ekjon Mayaboti', 25) # Create a new Person object

print(result.name, result.age)
print(result2.name, result2.age)
print(result2.greet())