
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_brand(self):
        return self.brand

    def set_brand(self, Newbrand):
        self.brand = Newbrand

    def get_color(self):
        return self.color

    def set_color(self,Newcolor):
        self.color = Newcolor

    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


c1 = Car("Toyota", "Red")
c2 = Car("BMW","Black" )

c1.display()
c2.display()

print("Brand:", c1.get_brand())

c1.set_brand("Honda")

print("New Brand:", c1.get_brand())

print("Brand:", c2.get_brand())
c2.set_brand("Scorpio Classic")
print("New Brand:", c2.get_brand())