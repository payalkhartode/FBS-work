
class A :
    def add(self):
        print("Add A")

class B :
    def add(self):
        print("Add B")

class C (B, A) :
    def add(self):
       print("Add C")

c1 = C()
c1.add()