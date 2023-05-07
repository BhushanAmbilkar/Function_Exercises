
# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# Given:
#
# def calculation(a, b):
#     # Your Code
#
# res = calculation(40, 10)
# print(res)

# Show Hint
# Separate return values with a comma.


# Show Solution
# In Python, to return multiple values from a function, use a comma to separate them

# Solution 1:
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)


# Solution 2:
def calculation(a, b):
    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)
