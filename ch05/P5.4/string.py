#Question: P5.4: Write a funtion
#def middle(string)
#that returns a string containing the middle character 
#in string if the length of string is odd, or the two middle characters 
#if the length is even. For example, middle("middle") returns "dd".

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 26th March, 2019

def main():
	string = input("Please enter any word of your choice: ")

	middle(string)

def middle(string):
	if len(string) % 2 == 0:
		print("The middle letters are " + string[len(string) // 2 - 1] + string[len(string) // 2])
	else:
		print("The middle letter is " + string[len(string) // 2])

main()
