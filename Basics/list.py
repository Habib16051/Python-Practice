digits = [10,20,30,40,50,60,70,80]
# adding at the end of list 
digits.append(30) 
digits[0] = 50 

# adding any position
digits.insert(5,100)

# Remove any value from the list
digits.remove(40)
# Delete any value from the list based on the index position
digits.pop(6)

print(digits)