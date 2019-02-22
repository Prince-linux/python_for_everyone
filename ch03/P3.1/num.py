#Question: P3.1: Write a program that reads an integer and prints whether it is negative, zero, or positive.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 21st February, 2019

num = float(input("Please Enter a number of your choice: "))

if num > 0:
	print("The number you gave as input is a positive number but not zero!")

elif num < 0:
	print("The number you gave as input is a negative number less than zero!")

else:
	print("The number you gave as input is zero!")