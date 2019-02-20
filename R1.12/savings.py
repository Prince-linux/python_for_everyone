''' A simple python program to calculate the number of years an account will be depleted

Question: R1.12: Write an algorithm to settle the following question: 
		A bank account starts out with $10,000. 
		Interest is compounded monthly at 0.5 percent per month. 
		Every month, $500 is withdrawn to meet college expenses.
	 	After how many years is the account depleted?

Author: Prince Oppong Boamah<regioths@gmail.com>
'''

balance = 10000
months = 0
expenses = 500

while balance > 500 :
        interest = balance * 0.005
        balance = balance + interest
        balance = balance - expenses
        print("Month: ", months, "Balance: ", balance)
       	months += 1
years = months / 12
print ("The account will be depleted in: ", years, "years")