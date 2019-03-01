#Question: P3.19: Write a program that prompts the user to provide a single character from the alpha­ bet. 
#Print Vowel or Consonant, depending on the user input.
# If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 1st March, 2019

letter = input("Please enter a single character from the alpha­bet: ")
if len(letter) > 1:
	print("Error! Please enter a single character")
elif not (letter.upper() and letter.lower()):
	print("Input is not a letter. Please enter a letter")
elif letter in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
	print("Input letter is a vowel")
elif letter.isdigit():
	print("Please enter a letter and not a number")
else:
	print("Input is a Consonant")




