#Question: P4.10: Write a program that reads a word and prints the number of vowels in the word.
#For this exercise, assume that a e i o u y are vowels. For example, if the user provides the input "Harry", the program prints 2 vowels.
#

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 5th March, 2019

word = input("Please Enter any word: ")
vowels = 0
for char in word :
	if  char.lower() in "aeiouy":
		vowels = vowels + 1
print("There are " + str(vowels) + " vowels in " + word)

