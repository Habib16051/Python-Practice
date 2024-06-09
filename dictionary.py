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
# adding new dicitonary in the dict ==> dict [key] = value
person['gender'] = 'male'
#  now the new dicitonary will be like that
print(person)

