



def max_num(first_num, second_num, third_num):
    maximum_number = 0

    if first_num > second_num:
        if first_num < third_num:
            maximum_number = third_num
        else:
            maximum_number = first_num

    else:
        if second_num > third_num:
            maximum_number = second_num
        else:
            maximum_number = third_num

    return maximum_number


def main():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))
    num3 = int(input("Please enter a final number: "))

    maximum = max_num(num1, num2, num3)

    print("The maximum of the three numbers you entered is " + str(maximum))

main()
