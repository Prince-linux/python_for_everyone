#Question: P6.3: Write a program that adds all numbers from 2 to 10,000 to a list. 
#Then remove the multiples of 2 (but not 2), multiples of 3 (but not 3), 
#and so on, up to the multiples of 100. Print the remaining values.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 28th March, 2019

nums = []
result = 0
for i in range(2, 10000):
	nums.append(i)
#print(nums)

for a in nums:
	for j in range(2, 100):
		if a % j == 0:
			nums.pop()
print(nums)




