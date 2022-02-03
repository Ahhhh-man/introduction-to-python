from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return 'Snakes use their tongues to smell.'


viper = Snake()

print(viper.use_tongue_to_smell())
print(viper.use_venom())
print(viper.hunt())