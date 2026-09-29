
class Emp:
    def __init__(self, nm):
        self.name = nm

    def display(self):
        print("Display")


class HR(Emp):
    def display(self):
        print("I am from display of Hr")


class SrHR(HR):
    def display(self):
        print("I am from display of Sr Hr")


class JrHR(SrHR):
    def display(self):
        print("I am from display of Jr Hr")


print("---- Multilevel Inheritance ----")
jhr = JrHR("Smriti")
jhr.display()