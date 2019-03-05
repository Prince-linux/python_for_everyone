num = input("Enter a sequence of sepreated integers: ")
number = num.split()
number = map(int, number)


for i in number:
	if i % 2 == 0:
		print('Even Number: ' + str(i))

	else:
		print('Odd Number: ' + str(i))