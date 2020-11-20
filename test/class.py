# This program tests how a class is initialized and inherited by a child class

class Adult():
    def __init__(self, name, age, gender, height, weight, eye_color):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def print_name(self):
        print(self.name)

class Kid(Adult):
    def print_cartoon(self, favorite_cartoon):
        print("{}'s favorite cartoon is {}".format(self.name, favorite_cartoon))

child = Kid("Andre", 0.9, "male", 2.3, 6.0, "black")

print(child.name)
print(child.age)
print(child.gender)
print(child.height)
print(child.weight)
print(child.eye_color)
child.print_name()
child.print_cartoon("Bugs Bunny")

