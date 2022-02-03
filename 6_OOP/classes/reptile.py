from animal import Animal


class Reptile(Animal):
    def __init__(self):
        super().__init__()  # `super` is used to inherit everything from parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return 'This Reptile is seeking heat.'

    def hunt(self):
        return 'This Reptile is hunting.'

    def use_venom(self):
        return 'This Reptile is venomous.'


# Creating an object of this Reptile class
lizard = Reptile()

print(lizard.seek_heat())
print(lizard.hunt())
print(lizard.use_venom())
# but we can also use animal methods via inheritance
print(lizard.breathe())
print(lizard.eat())
print(lizard.move())