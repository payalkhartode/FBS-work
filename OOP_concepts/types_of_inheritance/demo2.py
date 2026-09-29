
class Emp :
    def calSal(self):
        print("Employee salary")

class Hr(Emp) :
    def calSal(self):
        print("Hr salary")

class Admin(Emp) :
    def calSal(self):
        print("Admin salary")

h = Hr()
a = Admin()

h.calSal()
a.calSal()