# find.py: A program that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number
# Author: Prince Oppong Boamah
# Date: 2nd December, 2020


def search(my_list, user_input):
    for item in my_list:
        if item == user_input:
            return True
    return False



def main():
    my_list = []
    while True:
        item = raw_input("Please enter a number: ")
        if item == "no":
            break
        else:
            my_list.append(item)
            my_list.sort()
    num = raw_input("Please enter a number to see if i'ts available: ")
    print(my_list)
    print(search(my_list, num))

main()
