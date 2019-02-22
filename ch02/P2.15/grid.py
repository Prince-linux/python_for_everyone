#Question: P2.15: Printing a grid. Write a program that prints the following grid to play tic-tac-toe.
#				+--+--+--+ 
#				|  |  |	 | 
#				+--+--+--+ 
#				|  |  |  | 
#				+--+--+--+ 
#				|  |  |  | 
#				+--+--+--+
#				Of course, you could simply write seven statements of the form
#				print("+--+--+--+")
#				You should do it the smart way, though. Declare string variables to hold two kinds of patterns: a comb-shaped pattern and the bottom line. Print the comb three times and the bottom line once.
#
#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 20th February, 2019

comb_shaped = '+--+--+--+\n|  |  |  |\n'
bottom_shaped = '+--+--+--+\n'
print(comb_shaped + comb_shaped + comb_shaped + bottom_shaped)

