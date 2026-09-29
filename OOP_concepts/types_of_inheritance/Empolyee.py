
class Employee:

    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def getName(self):
        return self.name

    def setName(self,newName):
        self.name=newName

    def getSal(self):
        return self.sal

    def setSal(self,newsal):
        self.sal=newsal

    def getId(self):
        return self.id

    def setId(self,newid):
        self.id=newid

    def display(self):
        print(f"id={self.id}\tName={self.name}\tSal={self.sal}")

    def calSal(self):
        print("Employee Salary =",self.sal)

# Employee class Ends here........................

class Hr(Employee):

    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com=com

    def getCom(self):
        return self.com

    def setcom(self,newcom):
        self.com=newcom

    def calSal(self):
        print(f"Fianl HR Salary = {self.com+self.getSal()}")

# Hr class Ends here.............................

class Dev(Employee):

    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self,newbon):
        self.bonus=newbon

    def calSal(self):
        print(f"Fianl Developer Salary = {self.bonus+self.getSal()}")

# Devoloper class Ends here.............................

e = Employee(1,"Siya",50000)
h = Hr(2,"Joya",70000,1000)
d = Dev(3,"Radha",89650,100)


e.calSal()
h.calSal()
d.calSal()

