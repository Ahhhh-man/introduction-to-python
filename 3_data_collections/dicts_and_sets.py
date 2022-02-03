# Dictionaries and Sets are both data collections in Python

# Dictionaires are another way to manage data, but they have the advantage of being dynamic. Dict work as a KEY and VALUE.
# key: the reference of the object
# value: the desired data storage mechanism
# Syntax: name = { Key : Value } is used to declare a dict

student_1 = {
    'name': 'Alice',
    'stream': 'DevOps',
    'number_of_completed_lessons': 4,
    'completed_lesson_names': ['Variables', 'Data Types', 'Git and Github', 'Mathematical Operators'],
}

print(student_1)
print(student_1['stream'])
print(student_1['completed_lesson_names'][2])
print(type(student_1))

# Activity: Print penultimate index of key completed_lesson_names
print(student_1['completed_lesson_names'][-2])

# Applying CRUD
student_1['number_of_completed_lessons'] = 3
print(student_1['number_of_completed_lessons'])

# Removing an item from completed_lesson_names
student_1['completed_lesson_names'].remove('Variables')
print(student_1['completed_lesson_names'])

# We have some built-in methods within dict
# print all the keys using `keys()`
print(student_1.keys())
# print all the values using `values()`
print(student_1.values())

# Sets
# Sets are a collection of well-defined and distinct objects
# Syntax: name = {'','',''}

shopping_list = ['apple', 'banana', 'orange']
car_part = {'engine', 'tires', 'windows','engine'}

print(shopping_list)
print(car_part)
# Remark: Sets contain distinct objects, hence `'engine'` only appeared once

# Add items to sets
car_part.add('seats')
# Remove items from sets
car_part.remove('tires')

print(car_part)