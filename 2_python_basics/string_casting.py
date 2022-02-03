# Single and double quotes
single_quotes = 'These are single quotes and work perfectly fine!'
double_quotes = "These are double quotes and work perfectly fine!"

print(single_quotes)
print(double_quotes)

# Concatenation
First_Name = "James"
Last_Name  = "Bond"
print(First_Name + " " + Last_Name)

# Create a variable called age and display age in the same line as james bond
Age = 25
print(First_Name + " " + Last_Name + " is " + str(Age) + " years old.")

# Slicing and indexing
greetings = "Hello World!"
print(len(greetings))
print(greetings[0:10:2])        # slicing notation: sentence[<start>:<stop>:<step>],
print(greetings[-1])            # sentence[-1] = sentence[n] for n = len(sentence) - 1

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