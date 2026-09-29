
class Emp:
    def __init__(self, nm):
        self.name = nm
 
    def display(self):
        print("Display")
 
 
class HR(Emp):
    def display(self):
        print("I am from display of Hr")
 
 
print("---- Single Level Inheritance ----")
h1 = HR("Sachin")
h1.display()
