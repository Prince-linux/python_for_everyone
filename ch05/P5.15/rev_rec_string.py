#Question: P5.15: Write a recursive function
# def reverse(string)
#that computes the reverse of a string. 
#For example, reverse("flow") should return "wolf". 
#Hint: Reverse the substring starting at the second character, 
#then add the first character at the end. For example, to reverse "flow", 
#first reverse "low" to "wol", then add the "f" at the end.

#Author: Prince Oppong Boamah<regitohs@gmail.com>
#Date: 26th March, 2019

def main():
	string = input("Please enter any word of your choice: ")
	
	print("The original string  is : ",end="") 
	print(string)
	print("The reversed word(using recursion) is : ",end="")
	print(reverse(string))

def reverse(string):
	if len(string) == 0:
		return string
	else:
		return reverse(string[1:]) + string[0]

main()