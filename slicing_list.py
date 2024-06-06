colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

#  It  will slice the colors from index 1 to 3 (End - 1)
# sub_colors = colors[1:4]

# It will slice first four colors from the list which is equivalent to [0:4]
#  that means 0 to 3 (End - 1)
# sub_colors = colors[:4]


# It will slice last four colors from the list which is equivalent to [-4:]
#  that means -4 to -1 
# sub_colors = colors[-4:]
# print(sub_colors)

# The following example uses the step to return a sublist that includes every 2nd element of the colors list:

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[::2]

print(sub_colors)