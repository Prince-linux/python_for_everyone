#Question: P6.8: Compute the alternating sum of all elements in a list. 
#For example, if your program reads the input
#1 4 9 16 9 7 4 9 11
#then it computes
#1–4+9–16+9–7+4–9+11=–2

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 29th March, 2019

my_list = []
list_sum = 0

print("Please enter 10 numbers of your choice")
for i in range(10):
	num = input()
	my_list.append(num)
print(my_list)

for j in my_list[0::2]:
	list_sum = list_sum + int(j)
for j in my_list[1::2]:
	list_sum = list_sum - int(j)
print(list_sum)




