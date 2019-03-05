#Question: P4.1: Write programs with loops that compute
#a. The sum of all even numbers between 2 and 100 (inclusive).
#b. The sum of all squares between 1 and 100 (inclusive).
#c. All powers of 2 from 20 up to 220.
#d. The sum of all odd numbers between a and b (inclusive), where a and b are inputs.
#e. The sum of all odd digits of an input. (For example, if the input is 32677, the sum would be 3+7+7=17.)

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 4th March, 2019

#a
sum1 = 0

for i in range(0, 101):
	if i % 2 == 0:
		sum1 = sum1 + i
print(sum1)

#b
sum2 = 0
for a in range(0, 101):
	sum2 = sum2 + a * a

print(sum2)

#c
num = 2
sum3 = 0
while num <= 220:
	if num > 20:
		sum3 = sum3 + num 
	num = num * 2
	print(num)
#d

a = int(input('Please enter a number: '))
b = int(input('Please enter another number: '))
sum4 = 0
for i in range(a, b+1):
	sum4 = sum4 + 1
print(sum4)

#e
num2 = int(input('Please enter any number: '))
sum5 = 0

while num2 > 0:
	remainder = num2 % 10
	if remainder % 2 == 1:
		sum5 = sum5 + remainder
	num2 = num2 / 10
print(sum5)


