# parent class
class Anyone:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(self.firstname, self.lastname)
# child class
class Player(Anyone):
    pass
o1 = Player("Mo", "Salah")
o1.display()