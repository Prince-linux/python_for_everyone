# list2.py: A program that takes in user input into a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Author: Prince Oppong Boamah
# Date: 2nd December, 2020


def list_complete(user_list=[]):
    actual_list = []
    for i in user_list:
        if i not in actual_list:
            actual_list.append(i)
    return actual_list

def main():
    user_list = []
    while True:
        item = raw_input("Please enter any number: ")
        if item == "no":
            break
        else:
            user_list.append(int(item))
    print(user_list)
    print(list_complete(user_list))

main()

