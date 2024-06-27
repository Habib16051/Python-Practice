# square = lambda x : x**2

# print(f'The result is : {square(5)}')

#  A Lambda function is  python anonymous function without name; 
# A lambda expression typically contains one or more arguments, but it can have only one expression.

numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x : x ** 2, numbers))
print(result)