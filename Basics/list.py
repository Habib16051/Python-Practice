# What is a List?
# -------------------------------------------------------------------------------------------
# A list in Python is a collection of things (elements) stored in a particular order. The key points:
# The elements inside a list can be of different types (e.g., strings, numbers, booleans, even other lists) all together.
# The list remembers the order of its elements (so the first element keeps index 0, next index 1, etc.).
# You can access elements by their index. Also, negative indexing works (from the end) in Python lists.
# Lists are dynamic: you can change them after creating them (add, remove, modify elements).
# --------------------------------------------------------------------------------------------

digits = [10, 20, 30, 40, 50, 60, 70, 80, 30]

# adding at the end of a list
digits[0] = 50

# adding any position
digits.insert(5, 100)

# Remove any value from the list
digits.remove(40)

# Delete any value from the list based on the index position
digits.pop(6)

print(digits)
