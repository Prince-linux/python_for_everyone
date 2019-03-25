#Question: P5.1: Write the following functions and provide a program to test them.
#a. def smallest(x, y, z) (returning the smallest of the arguments) 
#b. def average(x, y, z) (returning the average of the arguments)

#Author: Prince Oppong Boamah<regioths@gmail.com
#Date: 25th March, 2019



def main():
	x = int(input("please enter your first number: "))
	y = int(input("Please enter your second number: "))
	z = int(input("Please enter your third number: "))
	smallest(x, y, z)
	average(x, y, z)

def smallest(x, y, z):
	if x < y and x < z:
		print(str(x) + " is the smallest")
	elif y < x  and y < z:
		print(str(y) + " is the smallest")
	else:
		print(str(z) + " is the smallest")

def average(x, y, z):
	k = x + y + z
	j = k / 3
	print("The average of the three numbers is " + str(j))

main()