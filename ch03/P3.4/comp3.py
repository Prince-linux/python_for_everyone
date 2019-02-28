#Question: P3.4: Write a program that reads three numbers and prints “all the same” if they are all the same, “all different” if they are all different, and “neither” otherwise.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 21st February, 2019

num1 = float(input("Please Enter your first number: "))
num2 = float(input("Please Enter your second number: "))
num3 = float(input("Please Enter your third number: "))

if num1 == num2 and num2 == num3:
	print("All the same")

elif num1 is not num2 and num1 is not num3 and num2 is not num1 and num2 is not num3 and num3 is not num1 and num3 is not num2:
	print("All different")

else:
	print("Neither")

	