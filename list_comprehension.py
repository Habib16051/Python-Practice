numbers = [10,20,30,40,50,60,70,80,90,100]

result = [number ** 2 for number in numbers]
print(result)

result2 = [number for number in numbers if number > 40]
print(result2)