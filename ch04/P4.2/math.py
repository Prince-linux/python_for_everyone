#Question: P4.2: Write programs that read a sequence of integer inputs and print a. 
#The smallest and largest of the inputs.
#b. The number of even and odd inputs.
#c.  Cumulative totals. For example, if the input is 1 7 2 9, the program should print
#181019.
#d. All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the program should print 3 5 6.

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 5th March, 2019

num = input("Enter a sequence of seperated integers: ")
number = num.split()
#number = map(int, number)

print('The maximum number is ' + str(max(number)))
print('The minimum number is ' + str(min(number)))




