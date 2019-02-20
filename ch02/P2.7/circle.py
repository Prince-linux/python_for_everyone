#Question: P2.7: Write a program that prompts the user for a radius and then prints
#				• The area and circumference of a circle with that radius
#				• The volume and surface area of a sphere with that radius
#
#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 20th February, 2019

radius = str(input("Please enter your radius: "))

pi = 3.14159

area = pi * (int(radius) * int(radius))
circumference = (2 * pi) * int(radius)
volume = (4 / 3) * area * int(radius)
surface_area = 4 * area
print("The area of  the circle is " + str(area) + " and it's circumference is " + str(circumference))

print("The volume of a sphere is " + str(volume) + " and the surface area is " + str(surface_area))
