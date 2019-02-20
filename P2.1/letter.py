'''Question: P2.1: Write a program that displays the dimensions of a letter­size (8.5 × 11 inch) 
					sheet of paper in millimeters. 
					There are 25.4 millimeters per inch. 
					Use constants and com­ ments in your program.

	Author: Prince Oppong Boamah<regioths@gmail.com>
'''

width = float(input("Please enter the width of your letter: "))
height = float(input("Please enter the height of your letter: "))

width = width * 25.4 
height = height * 25.4

print("Dimensions in mm are " + str(width) +" in width and in " + str(height) + " height")
