import random
import string
# 1 Day1 - Hello World
print("Hello World")

# 38 Day38 - Custom Errors
a = int(input("Enter any value between 5 and 9 :"))
if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")

# 42 Day 42 - Enumerate
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

# 43 Day43 - Virtual Environment
import pandas as pd
print(pd.__version__)

# 52 Day52 - Lambda Functions
def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 4))

# 53 Day53 - Map, Filter & Reduce
# ----------------------Map------------------------
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))

# ----------------------Filter------------------------
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

# ----------------------Reduce------------------------
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)

# 54 Day54 - is vs == in Python

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True
a = 5
b = 5
print(a == b)  # True
print(a is b)  # True