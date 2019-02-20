#Question: P2.11: Write a program that asks the user to input
#				•The number of gallons of gas in the tank
#				•The fuel efficiency in miles per gallon
#				•The price of gas per gallon
#				Then print the cost per 100 miles and how far the car can go with the gas in the tank.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 19th Febraury, 2019
gallons = float(input("Please enter the number of gallons in the tank: "))
fuel_efficiency = float(input("Please enter the fuel efficiency in miles: "))
gas_price = float(input("Please Enter the price of gas per gallon: "))
miles = int(fuel_efficiency) * int(gallons)
print("With gas price at " + str(gas_price) + " per gallon, 100 miles will cost you " + (str(gas_price * 100)))
print("With " + str(gallons) + "in the tank, you will only go " + str(miles) + " this far ")
