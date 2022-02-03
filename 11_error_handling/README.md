# Exception Handling

### Examples:
- `ValueError`
- `SyntaxError`
- `UnboundLocalError`
- `KeyError`
- `AttributeError`
- `ZeroDivisonError`
- `FileNotFoundError`

### File Permission

- `r` This is the default mode. It opens file for reading.
- `w` This mode opens file for writing. If the file doesn't exist, it creates a new one.
- `x` Creates a new file. If the file already exits, the operation fails
- `a` opens file in Append mode. If the file doesn't exist, it creates a new one.
- `t` This is the default mode to open text mode.
- `b` This is for binary mode.
- `+` This will open a file for reading and writing (updating).

we have `try`, `except` and `finally`,

- `try` works as `if` condition
- `except` as `elif`
- `finally` as `else`, and will execute regardless of try and except condition

## Activity
The functional code is [here](FileFinder/exception_handling_task.py).
```python
class FindFile:

    def find_file(self):
        found_file = False
        try:
            f = open("order.txt")
            f.close()
            found_file = True
        except FileNotFoundError as errmsg:
            found_file = False
        finally:
            return found_file

    def create_file(self):
        if not self.find_file():  # file doesnt exist
            f = open("order.txt", "x")  # create file
            f.close()  # close to reduce system resources
            return "Creating a new shopping List..."
        return "You have an existing Shopping list. Let's use this!"

    def read_file(self):
        print("Your shopping list is:")
        f = open("order.txt", "r")
        temp = f.read()
        f.close()
        return temp

    def write_file(self, item):
        f = open("order.txt", "a")
        temp = f.write(' - ' + item.title() + '\n')
        f.close()
        return temp
```

The main code is [here](main.py).
```python
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

```
