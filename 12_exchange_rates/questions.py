# Declare a function called username, that takes one argument as a string and return the name
"""
def username(username: str) -> str:
    return username


print(username('Alice'))
"""
# Declare a list with numbers 1 to 5; iterate through the list and display the list

"""
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
"""
# Which of the following returns a boolean: 'AND', '&', '&&' or '=='
"""
print(1 == 1)
"""
# What is the difference between a list and a tuple?
"""
- Lists are mutable, while tuples are not
- Tuples are initiated by simply separating the elements with a comma, with or without being enclosed by parentheses;
 while list are enclosed by square brackets.
"""
# Can we add an element to a list and tuples.
"""
# For List yes, for tuples No.

list = []
list.append(2)
"""
# Create a dictionary with key value first and last name
"""
name = {'firstname': 'first', 'lastname': 'last'}
"""
# Add and delete element from dictionary
""""
name = {'firstname': 'first', 'lastname': 'last'}

name['course'] = 'DevOps'
del name['key']
"""
# Create a class called student; initialise class and create an object of the class
"""
class Student:
    def __init__(self, name):
        self.name = name

devops_student = Student('Alice')
print(devops_student.name)
"""

# Create 2 functions that take 2 args each; one adds, the other subtracts
"""
def Func1(num1, num2):
    return num1 + num2


def Func2(num1, num2):
    return num1 - num2


print(Func1(10, 5))
print(Func2(10, 5))

# or equivalently...

Func1 = lambda x, y: x + y
Func2 = lambda x, y: x - y

print(Func1(10, 5))
print(Func2(10, 5))
"""
# Declare a dictionary with 3 shopping items with costs; eggs is 1.20, milk is 2.30 and bread is 1.00
"""
shopping_list = {
    'eggs': 1.20,
    'milk': 2.30,
    'bread': 1.00,
}

print(sum(price for price in shopping_list.values()))
"""

# Prompt the user to input a int, declare a func. that checks if the number is even or odd;
# and prints an appropriate message back
"""
check_even = lambda num: True if num % 2 == 0 else False

print('Even' if check_even(int(input('Number? '))) else 'Odd')
"""
# select the correct syntax-
# 1 -super.__init().
# 2- super()__init().
# 3 super().__init().
# 4 - Super().__init__()
"""
super().__init__()
"""
# Declare a tuple with three values of choice and iterate through them
"""
my_tuple = 'one', 'two', 'three'

for item in my_tuple:
    print(item)
"""
# Create a class called student with 1 method called student_data
# This function returns student name.
# Create a class called devops student which inherits student class
"""
class Student:
    def student_data(self, name):
        return name

class DevopsStudent(Student):
    def __init__(self):
        super().__init__()


person = DevopsStudent()
print(person.student_data('Alice'))
"""
# Task 15:
"""
city = 'London'


def is_london(city):
    return True if city == 'London' else False


print(is_london(city))
"""
# import sys and math, print the random method. Create a function that takes 2 args
"""
import random, sys, math


def percent_calc(x, y):
    return (x / y) * 100


print(percent_calc(random.randint(1, 100), random.randint(1, 100)))
"""