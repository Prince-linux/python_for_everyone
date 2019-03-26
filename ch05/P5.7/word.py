#Question: P5.7: Write a function
# def countWords(string)
#that returns a count of all words in the string string. 
#Words are separated by spaces.
#For example, countWords("Mary had a little lamb") should return 5.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 26th March, 2019

def main():

	string = input("Please Enter a word or phrase or sentence of your choice: ")
	countWords(string)

def countWords(string):
	word = string.split()
	print("Your input has " + str(len(word)) + " word(s)")

main()