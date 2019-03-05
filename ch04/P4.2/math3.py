num = input("Enter a sequence of sepreated integers: ")
number = num.split()


add_sum = number[0]
for i in number:
	print('Cumulative sum is ', str(add_sum))
	add_sum = add_sum + i