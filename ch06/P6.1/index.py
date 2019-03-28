#Question: P6.1: Write a program that initializes a list with ten random integers 
#and then prints four lines of output, containing
#• Every element at an even index.
#• Every even element.
#• All elements in reverse order.
#• Only the first and last element.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 27th March, 2019

import random

randNum = []

for i in range(10):
	randNum.append(random.randrange(1, 101, 1))
print(randNum )
print(str(randNum[0::2]) + " contains every element at even index")
print("the list beloW contains every even element")
for num in randNum:
		if num % 2 == 0:
			print(num, end=" ")
print("")
print(str(randNum[::-1]) + " is the random list in reverse order")

print(str(randNum[0]) + " is the first and " +str(randNum[9]) + " is the last element in the list" )

