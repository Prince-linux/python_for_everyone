#Qusetion: P2.4: Write a program that prompts the user for two integers and then prints
#				• The sum
#				• The difference
#				• The product
#				• The average
#				• The distance (absolute value of the difference)
#				• The maximum (the larger of the two)
#				• The minimum (the smaller of the two)
#				Hint: Python defines max and min functions that accept a sequence of values, each separated with a comma.
#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 19th February, 2019

num1 = str(input("Please enter your first number: "))
num2 = str(input("Please enter your second number: "))

add = int(num1) + int(num2)
print("The sum of the two numbers are " + str(add))
sub = int(num1) - int(num2)
print("The difference of the two numbers are " + str(sub))
mul = int(num1) *int(num2)
print("The product of the two numbers are " + str(mul))
avg = (int(num1) + int(num2)) / 2.0
print( "The average or mean of the two numbers are " + str(avg))
absolute = abs(sub)
print("The distance of the two numbers are " + str(absolute))

if num1 > num2:
	print("The maximum of the two numbers is " + str(num1))

else:
	print("The maximum of the two numbers is " + str(num2))

if num1 < num2:
	print("The minimum of the two numbers is " + str(num1))

else:
	print("The minimum of the two numbers is " + str(num2))
