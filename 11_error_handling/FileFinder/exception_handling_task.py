class FindFile:
    def find_file(self):
        found_file = False
        try:
            f = open("order.txt")
            f.close()
            found_file = True
        except FileNotFoundError:
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
