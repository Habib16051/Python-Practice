with open('read.txt') as f:
    lines = f.readlines()
    print(lines)

# Another way to read 
x = open('read.txt', 'r')
print(x.readlines())