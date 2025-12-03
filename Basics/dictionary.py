person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
print(person['first_name'])
print(person['last_name'])
print(person['favorite_colors'])
print(person['favorite_colors'][1])\

# using the get() method
print(person.get('age'))
# adding a new dictionary in the dict ==> dict [key] = value
person['gender'] = 'male'
#  now the new dictionary will be like that
print(person)

del person['active']
print(person)

# Using for loop

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}

for key, value in stocks.items():
    new_stocks[key] = value*2

print(new_stocks)

# using Python dictionary comprehension
new_stocks_2 = {key:value * 3 for (key, value) in stocks.items()}
print(new_stocks_2)