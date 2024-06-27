# An object has a state and behaviors. To create an object, you define a class first. 
# And then, from the class, you can create one or more objects. 
# The objects are instances of a class.

class Person:
    def __init__(self, name, age):
        self.name = name #instances of a person class
        self.age = age #another instances of a person class

result = Person('John',28) # Create a new Person object
result2 = Person('Mst Mobasshirin Mitu', 25) # Create a new Person object

print(result.name, result.age)
print(result2.name, result2.age)