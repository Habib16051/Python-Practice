lines = ['Lets write something interesting', 'If you miss the train i am on, you will know that i am gone']

with open('read.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')