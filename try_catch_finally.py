a = 10
b = 2

try:
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finishing up.')
