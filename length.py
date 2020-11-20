def str_length(str1, str2):
    
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)

user_input1 = str(input("Please enter any word: "))
user_input2 = str(input("Please enter another word: "))

str_length(user_input1, user_input2)
