for i in range(10):
    print('Hello')

names = []
while True:
    response = input('Add name? (y/n) ')
    if response.lower() == 'n':
        break
    temp_name = ' '.join(input("Name? ").title().split())
    names.append(temp_name)

print("Here is the list of name:", ', '.join(names))

list_names_lower = []
for name in names:
    list_names_lower.append(name.lower())

print(list_names_lower)

for i, x in enumerate(names):
    list_names_lower.append(names[i].lower())
    if len(names[i]) % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")