
class Mec:
    def display(self):
        print("I am from Mec")
 
 
class Electric:
    def display(self):
        print("I am from Electrical")
 
 
class Mecatronix(Electric, Mec):
    def abc(self):
        print("I am in Mecatronix")
 
 
print("---- Multiple Inheritance ----")
m = Mecatronix()
m.display()   # uses Electric's display() due to MRO (left-to-right)
m.abc()
print()
 