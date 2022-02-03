# Python Basics!
Python is a flexible, powerful, and general-purpose programming language.
### Why program in Python?
- Widely used within the industry
- Highly requested by clients
- Multi-purpose i.e., Artificial Intelligence
- Large programming community 
- Excellent online documentation 
- Endless libraries and packages 
- Powerful and flexible
### Python installation and PyCharm set up

- Test installation and PyCharm set up
- Python is a dynamically typed language

### Test environment and installation
Test first Python code with `print()`, enclosing a message.
```python
print("Hello World")
```
The output in the terminal should be:
```commandline
Hello World
```
## Variables
Variables are stored data values that can change during program execution.
```python
 First_Name = 'James'
 Last_Name = 'Bond'
 print('Hello {} {}!'.format(First_Name, Last_Name))
```
```commandline
Hello James Bond!
```
Remark: There are alternative ways to print statements. 
```python
print('Hello' + First_Name + Last_Name)
print(f'Hello {First_Name} {Last_Name}!')
```
### Understanding Variable Types
- strings: `Variable_Name = "Hello world"` or `Variable_Name = 'Hello world'`
- integers (ℤ): `Variable_Name = 5`
- floats (ℚ): `Variable_Name = 10.5`
```python
Word = 'Hello'
Integer_Num = 21
Floating_Num = 10.5

print(Word)
print(Integer_Num)
print(Floating_Num)
```
```commandline
Hello
21
10.5
```
## Activity 

- variables: `First_Name`, `Last_name`, `Age`, `Date_Of_Birth`
- Prompt user to input above values
- Print/display the type of each value received from the user
- then display the data back to the user with greeting message
### My Solution
```python
First_Name = input("What's your first name? ")
Last_name = input("What's your last name? ")
Age = input("What's your age? ")
Date_Of_Birth = input("What's your DoB (DD/MM/YYYY)? ")

# Test variable types
print(type(First_Name))
print(type(Last_name))
print(type(Age))
print(type(Date_Of_Birth))

# Remark: Only Age needs to changed from a string to an int
Age = int(Age)

# Print sentence
print(f'{First_Name} {Last_name} is {Age} yrs old and was born on {Date_Of_Birth}. I hope you enjoy your {Age + 1}th birthday next year!')
```


# What are Data Types and Operators
- Data Types are a type classification that describes the sort of value a variable has and what type of mathematical/logical operations may be done to it without generating an error. 
- A binary operation with the operator 🜨 on a set A is a map A×A → A, written (a,b) → a 🜨 b.

# Introduction to Python data types & Operators

Data types are the core of all programming languages. After all, if there is no data there is not a program.

Through the next few lessons we will be learning about all many of the data types available and more importantly some of the inbuilt methods around these data types that we can guarantee will be valuable to you as you progress.

Overall there are three high level data types that will be used:

1. Numbers: integers, longs, double, floating point numbers, etc.
2. Strings: Essentially any text
3. Boolean: true or false; 1 or 0 respectively 

We are very confident in saying that there is not a program anywhere that does not use, receive or deliver at a minimum one of the above data types.

# Operators

Operands are symbols that execute a particular mathematical or logical function and we will be using as many as possible throughout the lessons we will get around to using a large amount of them.

## Arithmetic Operators

| Operand    | Description                          | Example    |
|:---------: |:----------------------------:        |:--------:  |
|    +       | add two operands (variables) together| X + y + 2  |
|    -       | subtract two operands (variables)    | X - y - 2  |
|    *       | multiply two operands (variables)    | X - y - 2  |
|    /       | divide two operands (variables)      | X - y - 2  |
|    %       | Modulus - remainder of the division of left operand by the right    | X - y - 2  |
|    +       | add two operands (variables) together| X + y + 2  |

## Comparison Operators

| Operand    | Description                          | Example         |
|:---------: |:----------------------------:        |:--------:       |
|    >       | True if left operand is greater than the right| x > y  |
|    <       | True if left operand is less than the right| x < y     |
|    ==      | True if both operands are equal            | x == y    |
|    !=      | True if both operands are equal            | x != y    |
|    >=      | True if left operand is greater than or equal to the right| x >= y     |
|    <=      | True if left operand is less than or equal to the right| x <= y     |



Theses are just some of the examples and we will use many of them over this course.

## Examples
### Checking operations
```python
# Declare variables
num_1 = 10
num_2 = 5

# Print operations
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 % num_2)
print(num_1 ** num_2)

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)
```
# String Casting
## Single and double quotes
We can express a string in the following ways,
```python
single_quotes = 'These are single quotes and work perfectly fine!'
double_quotes = "These are double quotes and work perfectly fine!"

print(single_quotes)
print(double_quotes)
```
## Concatenation
Concatenation is when we join characters of strings end-to-end.
```python
First_Name = "James"
Last_Name  = "Bond"
print(First_Name + " " + Last_Name)
```
### Task
Create a variable called age and display age in the same line as james bond.
```python
Age = 25
print(First_Name + " " + Last_Name + " is " + str(Age) + " years old.")
```
## Slicing and indexing
```python
greetings = "Hello World!"
print(len(greetings))
print(greetings[0:10:2])        # slicing notation: sentence[<start>:<stop>:<step>],
print(greetings[-1])            # sentence[-1] = sentence[n] for n = len(sentence)

print(greetings[6:])
print(greetings[-6:])

white_spaces = "Helloooo                                                                         "
print(len(white_spaces))
print(len(white_spaces.strip()))

new_age = "10"
print(type(int(new_age)))

example_text = "lorem ipsum apple blah blah blah apple blah BLAH APPLE"
print(example_text.count("apple"))
print(example_text.lower())
print(example_text.lower().count("apple"))

print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace("blah", "..."))
```

