from FileFinder.exception_handling_task import FindFile

file = FindFile()
print(file.create_file())
while True:
    print(file.read_file())
    if input("Would you like to add another item? (y/n) ").lower() == 'n':
        break
    item = input("What would you like to add? ")
    file.write_file(item)

print('The Shopping list has been closed.')
