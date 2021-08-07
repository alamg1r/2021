# parent class
class Anyone:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(self.firstname, self.lastname)

# object
myObj = Anyone("Mo", "Salah")
myObj.display()