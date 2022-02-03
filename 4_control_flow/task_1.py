# Task
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