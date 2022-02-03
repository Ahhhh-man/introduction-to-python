class Animal:
    # we need to initialise with built-in method called `__init__(self)`
    # `self` refers to current file

    def __init__(self):  # we declare attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return 'Animals must keep breathing.'

    def eat(self):
        return 'Animals must keep eating.'

    def move(self):
        return 'Animals must keep moving.'


# we need to create an object of this class in order to use any methods
cat = Animal()

print(cat.breathe())
print(cat.eat())
print(cat.move())