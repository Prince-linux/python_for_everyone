#  A simple python code to split a series of characters convert to a dcitionary
query = 'user=james&database=master&password=sdhfjshfjhsafushuasf'
a_list = query.split('&')
print(a_list)
ab_list = [c.split('=', 1) for c in a_list]
print(ab_list)
ab_dict = dict(ab_list)
print(ab_dict)
