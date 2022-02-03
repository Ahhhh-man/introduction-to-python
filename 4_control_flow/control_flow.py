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

# Loops
shopping_list = ["apples", "banana", "orange", "kiwi", "grapes"]

# To print each element we could do,
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4])

# however this is tedious. Instead we can use `for` loops:
for items in shopping_list:
    if items == "orange":
        break
    print(items)

# infinite loops
# be careful not to create a never ending infinite loop as the program will never halt.

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


# We can create a while loop using `while`
num = 0
while num < 10:
    print(num, 'message')
    num += 1

print("--------------------------")  # temp

num = 0
while num < 10:
    print(num, 'message')
    if num == 5:
        break
    num += 1

# Let's see how can we interact with our user in the Third Iteration
# prompt the user to input age and restrict to enter in digits only
# check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits

age = input('What\'s your age? ')
while age.isdigit() == 0:
    age = input('What\'s your age? ')

print(age)

# alternative code using error handling

while True:
    try:
        age = int(input('What\'s your age? '))
    except ValueError:
        print("That's not an int!")
    else:
        print(age)
        break