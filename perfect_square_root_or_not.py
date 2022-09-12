import math  #importing math-module

# take inputs
num = int(input())

root = math.sqrt(num)
# check number is perfecct square
if int(root + 0.5) ** 2 == num:
    print('True')
else:
    print('False')