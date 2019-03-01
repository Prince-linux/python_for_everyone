#Question: P3.29: Write a program that asks the user to enter a month (1 for January, 2 for February, and so on) 
#and then prints the number of days in the month. For February, print “28 or 29 days”.
#Enter a month: 5 30 days
#Do not use a separate if/else branch for each month. Use Boolean operators.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 1st March, 2019

month = int(input("Please enter a month(1, for January, 2 for February and so on): "))

if month == 2:
	print("28 or 29 days in a leap year")

elif month <= 7:
	if month % 2 == 1:
		print("31 days")

	else:
		print("30 days")

else:
	if month % 2 == 1:
		print("30 days")
	else:
		print("31 days")
		