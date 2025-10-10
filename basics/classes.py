
"""
classes are blueprints for creating objects.
An object has properties and methods(functions) associated with it.

"""

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")  


dog = dog("Buddy", 3)
print(dog.name)
print(dog.age)
dog.bark()


#create a class of person and display name and age

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")   

person = person("krish", 30)
person.introduce()