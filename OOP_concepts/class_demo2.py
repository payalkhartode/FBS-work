
################ Static Variable ################################

class Student:

    inName = "FBS"

    def __init__(self,rollno, name, batch):

        self.rollno =rollno
        self.name=name
        self.batch = batch

    def display(self):
        print(f"RollNo={self.rollno}\t Name={self.name}\t batch={self.batch}\t Institute Name ={Student.inName}")

s1=Student(12,"Rakesh", "July Python")
s2=Student(13,"Rohit","July Python")
s3=Student(1,"Rakesh","June Python")

s1.display()
s2.display()
s3.display()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

Student.inName = "FirstBitSolutions"

s1.display()
s2.display()
s3.display()
