skills = {'Python programming','Databases', 'Software design'}
print(skills)

# You can use built in set() method to create set

skills_2 = set(['Python', 'Databases', 'Software design' 'Dhaka', 'Rangpur' ])
print(skills_2)

# Adding elements to a set
skills_2.add('Java')

print(skills_2)

# Removing an element from a set
skills_2.remove('Python')

print(skills_2)

#  You can also delete elements from a set using pop() method and discard()

# Frozen sets
skills = {'Problem solving', 'Software design', 'Python programming', 'Bangladesh'}
skills = frozenset(skills)
print(skills)
