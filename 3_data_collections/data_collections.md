# Python Data Collections
## List (aka. array in other languages)
  - Example: Shopping List
  - lists should be able to read and write entries i.e., Create, Read, Update and Delete (CRUD) 
  - Create a list: `list_name['item_1','item_2']`
  
We can create a shopping list using lists.
```python
shoppping_list = ["alpha", "beta", "gamma", "delta", "epsilon"]
print(shoppping_list)
```
```commandline
['alpha', 'beta', 'gamma', 'delta', 'epsilon']
```
We can check the data type of this list.
```python
print(type(shoppping_list))
```
```commandline
<class 'list'>
```
Using indexing for selective entries in the list.
```python
print(shoppping_list[1])
```
```commandline
beta
```
We can change an entry of a list using indexing.
```python
shoppping_list[0] = "not alpha"
print(shoppping_list[0])
print(shoppping_list[0:3])
```
```commandline
not alpha
['not alpha', 'beta', 'gamma']
```
Adding to the list using `append()`
```python
shoppping_list.append("omega")
print(shoppping_list)
```
```commandline
['not alpha', 'beta', 'gamma', 'delta', 'epsilon', 'omega']
```
Removing from the list using `remove()` or `pop()`
```python
shoppping_list.remove("gamma")
print(shoppping_list)

shoppping_list.pop(3)
print(shoppping_list)
```
```commandline
['not alpha', 'beta', 'delta', 'epsilon', 'omega']
['not alpha', 'beta', 'delta', 'omega']
```
The data types in a list don't have to be the same.
```python
mixed_list = ["Hello", 10 , 2.5]
print(mixed_list)
```
```commandline
['Hello', 10, 2.5]
```

# Tuples
```python
essentials = ('apple', 'banana', 'orange')
print(essentials)
print(type(essentials))
```
```commandline
('apple', 'banana', 'orange')
<class 'tuple'>
```
Remark: List are mutable, however tuples are not. Hence you cannot change, add or remove the data for tuples.

Additionally, the parentheses can be ignored for tuples.
```python
essentials = 'apple', 'banana', 'orange'
```


# Dictionaries and Sets 
Dictionaries and Sets are both data collections in Python.
Dictionaires are another way to manage data, but they have the advantage of being dynamic. Dict work as a KEY and VALUE.
- key: the reference of the object
- value: the desired data storage mechanism
- Syntax: name = { Key : Value } is used to declare a dict

```python

student_1 = {
    'name': 'Alice',
    'stream': 'DevOps',
    'number_of_completed_lessons': 4,
    'completed_lesson_names': ['Variables', 'Data Types', 'Git and Github', 'Mathematical Operators'],
}

print(student_1)
```
```commandline
{'name': 'Alice', 'stream': 'DevOps', 'number_of_completed_lessons': 4, 'completed_lesson_names': ['Variables', 'Data Types', 'Git and Github', 'Mathematical Operators']}
```
We can return selective values.
```python
print(student_1['stream'])
print(student_1['completed_lesson_names'][2])
```
```commandline
DevOps
Git and Github
```
Checking type within the dict.
```python
print(type(student_1))
```
```commandline
<class 'dict'>
```

### Activity: Print penultimate index of key completed_lesson_names
```python
print(student_1['completed_lesson_names'][-2])
```
```commandline
Git and Github
```

### Applying CRUD
```python
student_1['number_of_completed_lessons'] = 3
print(student_1['number_of_completed_lessons'])
```
```commandline
3
```

### Removing an item from completed_lesson_names
```python
student_1['completed_lesson_names'].remove('Variables')
print(student_1['completed_lesson_names'])
```
```commandline
['Data Types', 'Git and Github', 'Mathematical Operators']
```
### We have some built-in methods within dict

print all the keys using `keys()`
```python
print(student_1.keys())
```
```commandline
dict_keys(['name', 'stream', 'number_of_completed_lessons', 'completed_lesson_names'])
```
print all the values using `values()`
```python
print(student_1.values())
```
```commandline
dict_values(['Alice', 'DevOps', 3, ['Data Types', 'Git and Github', 'Mathematical Operators']])
```

# Sets
Sets are a collection of well-defined and distinct objects.
- Syntax: name = {'','',''}

```python
shopping_list = ['apple', 'banana', 'orange']
car_part = {'engine', 'tires', 'windows','engine'}

print(shopping_list)
print(car_part)
```
```commandline
['apple', 'banana', 'orange']
{'engine', 'windows', 'tires'}
```
Remark: Sets contain distinct objects, hence `'engine'` only appeared once

Add items to sets using `.add()`.
```python
car_part.add('seats')
```
Remove items from sets using `.remove()`.
```python
car_part.remove('tires')
print(car_part)
```
