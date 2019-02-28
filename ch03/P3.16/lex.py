#Question: P3.16: Write a program that reads in three strings and sorts them lexicographically.
#Enter a string: Charlie 
#Enter a string: Able 
#Enter a string: Baker 
#Able
#Baker 
#Charlie

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 28th February, 2019

string1 = input("Please enter three strings: ")
string2 = input("Please enter another string: ")
string3 = input("Please enter your last string: ")

words= [string1, string2, string3]
srted = sorted(words)
words.sort()

print(words[0])
print(words[1])
print(words[2])


