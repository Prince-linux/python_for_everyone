

def list_complete(user_list=[]):
    actual_list = []
    for i in user_list:
        if i not in actual_list:
            actual_list.append(i)
    return actual_list

a = [12, 32, 87, 2, 7, 12, 89, 87, 25, 13]

print(a)

print(list_complete(a))





        
