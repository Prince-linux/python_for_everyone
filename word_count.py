my_notes = input("Please enter a word, phrase, or sentence: ")

lower_case = sum(map(str.islower, my_notes))
upper_case = sum(map(str.isupper, my_notes)) 

print(my_notes)
print("UPPER CASE: %s" %(str(upper_case)))
print("LOWER CASE: %s" %(str(lower_case)))