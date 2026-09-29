
class Student:

    stdCount = 0

    def __init__(self,rollno, name, batch):

        self.rollno =rollno
        self.name=name
        self.batch = batch
        Student.stdCount += 1

    def getName(self):
        return self.name

    def setName(self,newName):
        self.name = newName

    def getBatch(self):
        return self.batch

    def setBatch(self,NewBatch):
        self.batch = NewBatch

    
    def display(self):
        print("Roll No = ",self.rollno)
        print("Name = ",self.name)
        print("Batch = ",self.batch)
        

class placeedStudent(Student):

    def __init__(self,rollno,name,batch,cName): 
        super().__init__(rollno,name,batch)
        self.cName = cName

    def getcName(self):
        return self.cName

    def setCname(self, NewCName):
        self.cName = NewCName

    def display(self):
        super().display()
        print("CName = ",self.cName)
        print()
       
s1=Student(1,"Siya", "July Python")
s2=Student(2,"Radha","July Python")
s3=Student(3,"Ram","June Python")

s4 = placeedStudent(13, "Shivam", "June-2015", "GlobalPayment")


s1.display()
print()

s2.display()
print()

s3.display()
print()

s4.display()
print()

print(Student.stdCount)