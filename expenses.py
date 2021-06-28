exp = [800, 1000, 1500, 2000, 3000]
total = 0

for i in range(len(exp)):
   print('Month:', (i+1), 'Expenses:', exp[i])
   total = total + exp[i]

print('Total expenses:', total) 
   
