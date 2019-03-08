#Question: P4.17: Prime numbers. 
#Write a program that prompts the user for an integer 
#and then prints out all prime numbers up to that integer. 
#For example, when the user enters 20, the program should print
#   2
#   3
#   5
#   7
#   11
#   13
#   17
#   19
#Recall that a number is a prime number if it is not divisible by
# any number except 1 and itself.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 8th March, 2019

num = int(input("Please enter a number: "))

for i in range(1, num):
	j = 2
	counter = 0

	while j < i:
		if i % j ==0:
			counter = 1
			j = j + 1

		else:
			j = j + 1

	if counter == 0:
		print(i)
	else:
		counter = 0