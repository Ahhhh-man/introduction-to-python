from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return 'A python can digest large animals.'

    def climb(self):
        return 'A python can climb.'

    def __shed_skin(self):
        return 'A python can shed its skin.'


python = Python()

print(python.digest_large_prey())
print(python.use_tongue_to_smell())
print(python.use_venom())
print(python.hunt())

# print(python.__shed_skin())