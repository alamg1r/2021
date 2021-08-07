# many objects on the same class
class NewClass:

    def NewHello(self):
        return "Hello from the NewHello function"

# first object
first_object = NewClass()
print(first_object.NewHello())

# second object
second_object = NewClass()
print(second_object.NewHello())
