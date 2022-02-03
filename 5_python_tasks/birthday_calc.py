from datetime import datetime

CURRENT_YEAR = datetime.now().year
CURRENT_MONTH = datetime.now().month
name = 'Alice'
age = '21'
birth_day = 25
birth_month = 12

# Calc. year diff
year_diff = CURRENT_YEAR - int(age)
if CURRENT_MONTH < birth_month:
    year_diff -= 1

print(f'Hi {name}, you are {age} years old so you were born in {year_diff}.')

#==================================================================================
def req(message):
    temp = input(message)
    while not temp.isdigit():
        print('Invalid Input. Try again.')
        temp = input(message)
    return int(temp)

# Request inputs
name = ' '.join(input("What's your name? ").title().split())
age = req("What\'s your age? ")
birth_day = req("What\'s your birth day? ")
birth_month = req("What\'s your birth month? ")

# calc year diff
year_diff = CURRENT_YEAR - int(age)
if CURRENT_MONTH < birth_month:
    year_diff -= 1

# print statements
print(f'Hi {name}, you are {age} years old so you were born in {year_diff}.')
print(f'You have lived for {(datetime.now() - datetime(year_diff, birth_month, birth_day)).days * 24} hours!')