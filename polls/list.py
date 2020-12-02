# list2.py: A program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Author: Prince Oppong Boamah
# Date: 2nd December, 2020

def list_complete(user_list=[]):
    actual_list = []
    for i in user_list:
        if i not in actual_list:
            actual_list.append(i)
    return actual_list

a = [12, 32, 87, 2, 7, 12, 89, 87, 25, 13]

print(a)

print(list_complete(a))





        
