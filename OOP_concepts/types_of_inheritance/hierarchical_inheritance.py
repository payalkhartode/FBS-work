
class Emp:
    def __init__(self, nm):
        self.name = nm

    def display(self):
        print("Display")


class Dev(Emp):
    def display(self):
        print("I am from display of Dev")


class HR2(Emp):
    def display(self):
        print("I am from display of Hr (HR2)")


print("---- Hierarchical Inheritance ----")
d1 = Dev("Pradip")
d1.display()

h2 = HR2("Pranjali")
h2.display()