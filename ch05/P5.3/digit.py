#Question: P5.3: Write the following functions.
#a. def firstDigit(n) (returning the first digit of the argument) 
#b. def lastDigit(n) (returning the last digit of the argument)
#c. def digits(n) (returningthenumberofdigitsoftheargument)
#For example, firstDigit(1729) is 1, 
#lastDigit(1729) is 9, and digits(1729) is 4. 
#Provide a program that tests your functions.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 25th March, 2019

def main():
	num = input("Please enter your number: ")
	firstDigit(num)
	lastDigit(num)
	digits(num)

def firstDigit(num):
	print ("The first number of your input is " + str(num[0]))

def lastDigit(num):
	num1 = int(num) % 10
	print("The last number or digit of your input is " + str(num1))

def digits(num):
	print("The length of your input is " + str(len(num)))

main()
