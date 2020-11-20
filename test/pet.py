# this is a program to test the composition of a class in python 

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

dre = Person("Andre Boamah")

dog = Dog("Emelia", "German Shepherd", dre)

print(dog.owner)

