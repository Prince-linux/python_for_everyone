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

