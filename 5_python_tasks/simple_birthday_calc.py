name = ' '.join(input("What's your name? ").title().split())

age = input('What\'s your age? ')
while not age.isdigit():
    print('Invalid Input. Try again.')
    age = input('What\'s your age? ')

year_diff = 2021 - int(age)
print(f'Hi {name}, you are {age} years old so you were born in {year_diff}.')
print(f'You have lived for {int(age) * 365 * 24} hours!')