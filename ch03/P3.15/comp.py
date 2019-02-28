#Question: P3.15: Write a program that reads in three floating­point numbers 
#and prints the largest of the three inputs without using the max function.
#For example:
#Enter a number: 4
#Enter a number: 9
#Enter a number: 2.5
#The largest number is 9.0

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 22nd February, 2019

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
num3 = float(input("Please enter your third number: "))

if num1 > num2 and num1 > num3:
	print(str(num1) + " is the greatest")

elif num2 > num1 and num2 > num3:
	print((str(num2) + " is the greatest"))

else:
	print((str(num3) + " is the greatest"))