#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method1")

    def method2 (self, someString):
        print("myClass method2 " + someString)

class aClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("aClass method1")

    def method2 (self, someString):
        print("aClass method2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("This is AA")
    c2 = aClass()
    c2.method1()

if __name__ == "__main__":
    main()
