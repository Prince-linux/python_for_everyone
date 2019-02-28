#Question: P3.17: Write a program that reads in a string and prints whether it
#• contains only letters.
#• contains only uppercase letters.
#• contains only lowercase letters.
#• contains only digits.
#• contains only letters and digits.
#• starts with an uppercase letter.
#• ends with a period.

string1 = input("PLease enter a string: ")

if string1.isalpha():
	print(" The string you provided contains only letters")
elif string1.isalnum():
	print("The string you provided contains only letters and digits")

elif string1.islower():
	print("The string you provided contains only lowercase letters")
elif string1.isupper():
	print("The string you provided contains omly uppercase letters")
elif string1.isdigit():
	print("The string you provided contains only digits")

elif string1[0].isupper():
	print("The string you provided starts with an uppercase letter")
elif string1.endswith('.'):
	print("The string you provided ends with a period")





