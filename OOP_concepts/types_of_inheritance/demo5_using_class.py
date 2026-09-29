
class Addition:
    def __init__(self, a, b, s1, s2, l1, l2):
        self.a = a
        self.b = b
        self.s1 = s1
        self.s2 = s2
        self.l1 = l1
        self.l2 = l2

    def add_integers(self):
        result = self.a + self.b
        print(result)

    def add_strings(self):
        result = self.s1 + self.s2
        print(result)

    def add_lists(self):
        result = self.l1 + self.l2
        print(result)



A = Addition(10, 20, "Virat ", "Koholi", [1, 2, 3], [4, 5, 6])

A.add_integers()
A.add_strings()
A.add_lists()