#Question: P6.16: Write a program that generates a sequence of 20 random values 
#between 0 and 99 in a list, prints the sequence, 
#sorts it, and prints the sorted sequence. Use the list sort method.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 29th March, 2019

import random

randNum = []

for i in range(20):
	num = random.randint(0, 100)
	if num not in randNum:
		randNum.append(num)
print(randNum)
randNum.sort()
print(randNum)

