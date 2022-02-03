# Control flow
We can use `if`, `elif` and `else` to create an if-condition.
```python
weather = 'sunny'

if weather == 'sunny':
    print('Enjoy the weather!')
elif weather == 'rainy':
    print('Under my umbrella, ella, ella, eh, eh, eh')
else:
    print('Unknown weather!')

if weather != 'sunny':
    print('Well it\'s not sunny! I\'d stay at home.')


age = 18
if age < 18:
    print('You are too young to drive!')
```
# Activity
## Task 1
```python
names = []
add_people = 0
while add_people == 0:
    response = input('Would you like to add someone? (y/n) ')
    if response.lower() == 'y':
        temp = input('Who? ')
        temp = " ".join(temp.split())
        names.append(temp.title())
    elif response.lower() == 'n':
        add_people = 1
    else:
        print('Invalid input.')
        pass

# v1
if not names:
    print('Welcome everyone to Sparta Global!')
else:
    print('Welcome {} and {} to Sparta Global!'.format(', '.join(names[0:-1]), names[-1]))

# v2
welcome_message_start = "Welcome"
welcome_message_mid = "and"
welcome_message_end = "to Sparta Global!!"
welcome_message_full = 'Welcome everyone to Sparta Global!'

if not names:
    print(welcome_message_full)
else:
    print(welcome_message_start,', '.join(names[0:-1]),welcome_message_mid, names[-1] , welcome_message_end)
```
## Task 2
### Movie Ratings!
As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

check for rating for this movie:
- universal -> everyone can watch
- pg --> General viewing, but some scenes may be unsuitable for young children
- 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
- 15 --> No one younger than 15 may see a 15 film in a cinema.
- 18 --> No one younger than 18 may see an 18 film in a cinema.
```python
# Request user age
age = int(input('What\'s your age? '))
# Assume movie rating is given
movie_rating = '15'

if movie_rating == '18' and age >= 18:
    print('You can watch this "Suitable only for adults 18+" film')
elif movie_rating == '15' and age >= 15:
    print('You can watch this "Suitable only for 15 years and over" film')
elif movie_rating == '12' and age >= 12:
    print('You can watch this "Suitable for 12 years and over" film')
elif movie_rating == 'pg':
    print('You can watch this "PG Parental Guidance" film')
elif movie_rating == 'U':
    print('You can watch this "U Universal - Suitable for all')
else:
    print('Sorry you can\'t watch this {} film'.format(movie_rating))
```

# Loops
Loops help us iterate between our data i.e. lists, dict or sets.
```python
shopping_list = ["apples", "banana", "orange", "kiwi", "grapes"]
```
To print each element we could do,
```python
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4])
```
```commandline
apples
banana
orange
kiwi
grapes
```
However this is tedious. Instead we can use `for` loops:
```python
for items in shopping_list:
    print(items)
```
```commandline
apples
banana
orange
kiwi
grapes
```
Remark: Be careful not to create a never ending infinite loop as the program will never halt.
```python
student_data = {
    'student_name': 'Alice',
    'course': 'DevOps',
    'course_topics': 4,
    'topic_names': ['Business Week', 'Python', 'Virtualisation with Vagrant', 'AWS Cloud'],
}
print(student_data)

for data in student_data.values():
    if data == 'Alice':
        print(data)
```
```commandline
{'student_name': 'Alice', 'course': 'DevOps', 'course_topics': 4, 'topic_names': ['Business Week', 'Python', 'Virtualisation with Vagrant', 'AWS Cloud']}
Alice
```

# While loops
We can create a while loop using `while`
```python
num = 0
while num < 10:
    print(num, 'message')
    num += 1
``` 
```commandline
0 message
1 message
2 message
3 message
4 message
5 message
6 message
7 message
8 message
9 message
```
If we want to break out of a while loop, we can use `break`.
```python
num = 0
while num < 10:
    print(num, 'message')
    if num == 5:
        break
    num += 1
```
```commandline
0 message
1 message
2 message
3 message
4 message
5 message
```
## Activity
Let's see how can we interact with our user in the Third Iteration

- prompt the user to input age and restrict to enter in digits only
- check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits

```python
age = input('What\'s your age? ')
while age.isdigit() == 0:
    age = input('What\'s your age? ')

print(age)
```
Alternative code using error handling
```python
while True:
    try:
        age = int(input('What\'s your age? '))
    except ValueError:
        print("That's not an int!")
    else:
        print(age)
        break
```