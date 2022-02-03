# Strings
First_Name = 'Aman'
Last_Name = 'Uddin'
print('Hello {} {}!'.format(First_Name, Last_Name))


# Numbers
Num1 = 10 # int
Num2 = 10.5 # float
Num3 = 10.54423424 # double
print(Num3)

# Input
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