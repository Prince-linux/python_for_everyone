number = int(input("Please enter any number: "))

if number % 4 ==0:
    print("%s is a Multiple of 4" %(str(number)))
elif number % 2 ==0:
    print("%s is an Even Number" %(str(number))) 
else:
     print("%s is an Odd Number" %(str(number)))


num = int(input("Please enter first number: "))
check = int(input("Please enter second number: "))
if num % check == 0:
    print("Both numbers Divide evenly")
else:
    print("Can't Divide both numbers evenly")

