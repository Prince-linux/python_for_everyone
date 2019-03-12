#Question: P4.21: Write a program that reads an integer and displays, 
#using asterisks, a filled and hol- low square, placed next to each other. 
#For example if the side length is 5, the program should display
#	***** ***** 
#	***** *   * 
#	***** *   * 
#	***** *   * 
#	***** *****

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 8th March, 2019

side_length = int(input("Please enter the side length: "))
inner_size = side_length - 2
print ('*' * side_length + '  ' + '*' * side_length)
for i in range(inner_size):
    print ('*'  * side_length + '  ' + '*' + ' ' * inner_size + '*')
print ('*' * side_length + '  ' + '*' * side_length)
