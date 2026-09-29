
class Emp :
    def calSal(self):
        print("Employee salary")

class Hr(emp) :
    def calSal(self):
        print("Hr salary")

class Admin(Emp ,Hr ) :
    def calSal(self):
        print("Admin salary")

h = Hr()
a = Admin()

h.calSal()
a.calSal()