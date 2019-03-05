numbers = input("Enter a list element separated by space ")
list  = input_string.split()
list = map(int, list)
 
#first solution
 
print(min(list))
print(max(list))
 
#second problem solution
 
for i in list:
  	if(i%2==0):
     	print("even number- ", i)
  	else
     	print("odd number- ", i)
 
#third problem solution
 
sum = list[0]
for i in list:
     print("cumulative sum is - ", sum)
     sum+=i