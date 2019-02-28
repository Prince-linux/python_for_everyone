# Question: P3.7: Write a program that reads in three integers and prints “in order” if they are sorted in ascending or descending order, or “not in order” otherwise. For example,
#1 2 5 in order 
#1 5 2 not in order
#5 2 1 in order
#1 2 2 in order

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 22nd February, 2019

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
num3 = float(input("Please enter your third number: "))

if num1 < num2 and num2< num3:
	print("in order")
elif num1 > num2 and num2 > num3:
	print("in order")
elif num1 < num2 and num2 <= num3:
	print("in order")
elif num1 > num2 and num2 >= num3:
	print("in order")
else:
	print("not in order")


