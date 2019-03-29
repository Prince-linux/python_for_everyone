#Question: P6.7: Write a function removeMin that removes 
#the minimum value from a list without using the min function or remove method.

#Author: Prince Opppong Boamah<regioths@gmail.com>
#Date: 29th March, 2019

num = [20, 10 , 2, 4, 5, 6, 7]
def removeMin(num):
	for i in num:
		if i < num[num.index(i)-1]:
			min_value = i
	print(min_value)
	print(num)
	num.pop(min_value)
	print(num)

removeMin(num)


