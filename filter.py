#  Normal way to filter out the following list of elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

filtered = []

for i in numbers:
    if i % 2 == 0:
        filtered.append(i)


print(filtered)
