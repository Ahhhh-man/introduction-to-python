# Zero division error: We can create an mathematical error by dividing by zero
# print(1 / 0)

# Type error:
# num = 9
# if num > 'Hello':
#     print(num)

# We will create a file with required permission and see what error/exception are observable

# First Iteration
# file = open("order.txt")  # `open()` takes a string arg with file name
# print(file)

# Second Iteration

try:
    file = open("order.txt")
    print("File found")
except FileNotFoundError as errmsg:
    print("File not found: {}".format(errmsg))
    # raise
finally:
    print('Goodbye')
