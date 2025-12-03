rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)

#  We can use set union another way
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1 | s2

print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {7, 9, 12, 19, 20, 3}

s = s1 | s2

print(s)
