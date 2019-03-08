#Question: P4.22: Write a program that reads an integer and displays, 
#using asterisks, a filled diamond of the given side length.
# For example, if the side length is 4, the program should display
#       * 
#      *** 
#     ***** 
#    ******* 
#     ***** 
#      ***
#       *

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 8th March, 2019


rows = int(input("Please enter number of rows: ")) 
n = 0
for i in range(1, rows + 1): 
    for j in range (1, (rows - i) + 1): 
        print(end = " ") 

    while n != (2 * i - 1): 
        print("*", end = "") 
        n = n + 1
    n = 0 
    print()  
  
k = 1
n = 1
for i in range(1, rows): 
    for j in range (1, k + 1): 
        print(end = " ") 
    k = k + 1

    while n <= (2 * (rows - i) - 1): 
        print("*", end = "") 
        n = n + 1
    n = 1
    print() 
  