#Question: P3.12: Write a program that translates a letter grade into a number grade. 
#Letter grades are A, B, C, D, and F, possibly followed by + or –. 
#Their numeric values are 4, 3, 2, 1, and 0. There is no F+ or F–. 
#A + increases the numeric value by 0.3, a – decreases it by 0.3. 
#However, an A+ has value 4.0.

#Author:Prince Oppong Boamah<regitohs@gmail.com>
#Date: 22nd February, 2019

grade = input("Please enter a grade: ")

GRADE_A = 4.0
GRADE_B = 3.0
GRADE_C = 2.0
GRADE_D = 1.0
GRADE_F = 0

if grade == "A" or grade == "a" or grade == "A+":
	print("Your grade's value is " + str(GRADE_A))
elif grade == "A-" or grade == "a-":
	print("Your grade's value is " + str(float(GRADE_A) - 0.3))
elif grade == "B" or grade == "b":
	print("Your grade's value is " + str(GRADE_B))
elif grade == "B+" or grade == "b+":
	print("Your grade's value is " + str(float(GRADE_B) + 0.3))
elif grade == "B-" or grade == "b-":
	print("Your grade's value is " + str(float(GRADE_B) - 0.3))
elif grade == "C" or grade == "c":
	print("Your grade's value is " + str(GRADE_C))
elif grade == "C+" or grade == "c+":
	print("Your grade's value is " + str(float(GRADE_C) + 0.3))
elif grade == "C-" or grade == "c-":
	print("Your grade's value is " + str(float(GRADE_C) - 0.3))
elif grade == "D" or grade == "d":
	print("Your grade's value is " + str(GRADE_D))
elif grade == "D+" or grade == "d+":
	print("Your grade's value is " + str(float(GRADE_D) + 0.3))
elif grade == "D-" or grade == "d-":
	print("Your grade's value is " + str(float(GRADE_D) - 0.3))
elif grade == "F" or grade =="f":
	print("Your grade's value is " + str(GRADE_F))
else:
	print("You entered an invalid grade")

	

