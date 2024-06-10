#  A basic intro of list comprehension
numbers = [10,20,30,40,50,60,70,80,90,100]

result = [number ** 2 for number in numbers]
print(result)

# when we want to add any condition in the list comprehension
result2 = [number for number in numbers if number > 40]
print(result2)

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

selected_stocks = {s: p for (s, p) in stocks.items() if p > 220}

print(selected_stocks)