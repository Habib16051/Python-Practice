from functools import reduce

scores = [10, 20, 30, 40, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)