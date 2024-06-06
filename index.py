cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico', 'Osaka']
city = 'Osaka'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
